from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes.tts import tts_bp
    app.register_blueprint(tts_bp, url_prefix='/api/tts')

    return app
