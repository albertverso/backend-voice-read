from flask import Blueprint, request, send_file, jsonify
from app.services.tts_engine import generate_audio
import os

tts_bp = Blueprint('tts', __name__)

@tts_bp.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Texto não fornecido'}), 400

    text = data['text']

    # Gera o caminho do áudio
    audio_path = generate_audio(text)

    if not os.path.exists(audio_path):
        return jsonify({'error': 'Erro ao gerar áudio'}), 500

    absolute_path = os.path.abspath(audio_path)

    return send_file(absolute_path, mimetype='audio/mpeg')

    # return jsonify({'message': 'Áudio gerado com sucesso'}), 200