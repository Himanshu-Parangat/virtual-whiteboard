from flask import Flask
from app.routes import main_routes

def create_app():
    app = Flask(__name__, static_folder='assets', static_url_path='/assets', template_folder='components')
    app.register_blueprint(main_routes)

    return app
