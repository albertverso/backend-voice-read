import easyocr
from PIL import Image
import numpy as np

reader = easyocr.Reader(['pt'], gpu=False)  # Carrega uma vez para reuso

def extract_text_to_imagem(image_stream):
    """
    Recebe um arquivo de imagem (stream) e retorna o texto extraído.
    """
    image = Image.open(image_stream).convert('RGB')
    result = reader.readtext(np.array(image), detail=0)
    text = " ".join(result)
    return text
