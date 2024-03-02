from flask import Flask
app = Flask(__name__, static_folder='assets', static_url_path='/assets', template_folder='components')
from app import routes


