from flask import Blueprint, request, jsonify
from app.services.link_extractor_engine import extract_content_from_url

extrair_url_bp = Blueprint('extrair_url', __name__)

@extrair_url_bp.route('/extract', methods=['POST'])
def extrair_texto_url():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'status': 400, 'message': 'URL não fornecida.'}), 400

    try:
        resultado = extract_content_from_url(url)
        return jsonify({'status': 200, **resultado})
    
    except Exception as e:
        return jsonify({'status': 500, 'message': str(e)}), 500
