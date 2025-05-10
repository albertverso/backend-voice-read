from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    API_KEY = os.getenv("GEMINI_API")