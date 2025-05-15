from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}}) 

    from .routes.tts import tts_bp
    # from .routes.ocr import ocr_bp
    from .routes.gemini import gemini_bp
    from .routes.link_extractor import extrair_url_bp

    app.register_blueprint(extrair_url_bp, url_prefix='/api')
    app.register_blueprint(gemini_bp, url_prefix='/api')
    app.register_blueprint(tts_bp, url_prefix='/api')
    # app.register_blueprint(ocr_bp, url_prefix='/api')

    return app
