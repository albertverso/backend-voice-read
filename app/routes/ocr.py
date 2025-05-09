from flask import Blueprint, request, jsonify
from app.services.ocr_engine import extract_text_to_imagem

ocr_bp = Blueprint('ocr', __name__)

@ocr_bp.route('/ocr', methods=['POST'])
def ocr_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhum arquivo de imagem enviado'}), 400

    imagem = request.files['image']
    try:
        text = extract_text_to_imagem(imagem.stream)
        return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500