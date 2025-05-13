import google.generativeai as genai
from app.config import Config
from PIL import Image
import re

# Configurando a chave da API
genai.configure(api_key=Config.API_KEY)

def generate_text_from_image(image_path: str):
    # Abrindo a imagem usando PIL
    image = Image.open(image_path)
    
    # Criando o modelo
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Gerando conteúdo a partir da imagem
    response = model.generate_content(["Analise a imagem e transcreva seus textos em português(não precisa separar os textos por '\n' somente dê espaço): ", image])

    text = response.text
    
    return text