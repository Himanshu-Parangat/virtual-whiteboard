from .utils import genrate_frames
from flask import render_template, Response
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture')
def stream():
    return Response(genrate_frames(True), mimetype='multipart/x-mixed-replace; boundary=frame')
