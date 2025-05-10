from app.services.gemini_engine import generate_text_from_image
from flask import Blueprint, request, jsonify
from PIL import Image

gemini_bp = Blueprint('gemini', __name__)

@gemini_bp.route('/gemini', methods=['POST'])
def gemini_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhum arquivo de imagem enviado'}), 400

    imagem = request.files['image']
    try:
        text = generate_text_from_image(imagem)
        return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        