from flask import render_template, Response, Blueprint
from .utils import genrate_frames



# Define a blueprint named 'main'
main_routes = Blueprint('main', __name__)

# Define your routes within the blueprint
@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/board')
def stream():
    return Response(genrate_frames(True), mimetype='multipart/x-mixed-replace; boundary=frame')
