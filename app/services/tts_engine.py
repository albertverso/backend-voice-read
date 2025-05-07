from gtts import gTTS
import uuid
import os

def generate_audio(text):
    filename = f"{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("temp_audio", filename)

    os.makedirs("temp_audio", exist_ok=True)

    tts = gTTS(text=text, lang='pt-br')
    tts.save(filepath)

    return filepath

    # return jsonify({'message': 'Áudio gerado com sucesso'}), 200