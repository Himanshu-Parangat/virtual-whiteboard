from flask import render_template, Response, Blueprint
import cv2


# Define a blueprint named 'main'
main_routes = Blueprint('main', __name__)

# Define your routes within the blueprint
@main_routes.route('/')
def index():
    return render_template('index.html')

def genrate_frames(capture_state):
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Unable to open camera.")
        return 

    while capture_state:
        sucess,frame=camera.read()
        if not sucess:
            print("Error: Failed to read frame.")
            break
        else:
            ret,buffer=cv2.imencode('.png',frame)
            frame=buffer.tobytes()

        yield (b'--frame\r\n'
                b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

@main_routes.route('/board')
def stream():
    return Response(genrate_frames(True), mimetype='multipart/x-mixed-replace; boundary=frame')
