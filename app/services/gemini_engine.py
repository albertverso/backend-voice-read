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
    response = model.generate_content(["Trascreva o texto analise pode ser um texto normal ou um print de uma conversa mas lembrando somente a parte das falas de aplicativo de mensagens, geralmente whatsapp, telegram, instagram onde as falas sao representadas por balões de falas(não precisa separar os balaões por '\n' somente dê espaço):", image])

    text = response.text
    
    return text