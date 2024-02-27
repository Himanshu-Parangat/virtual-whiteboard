import cv2

def genrate_frames(capture_state):
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FPS, 30)
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
