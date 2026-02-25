from flask import Flask, render_template, Response
import cv2
from liveness import check_face
from auth_token import generate_token
import time

app = Flask(__name__)

camera = None


# ==============================
# HOME PAGE
# ==============================
@app.route('/')
def home():
    return render_template('index.html')


# ==============================
# VIDEO FEED (Live Camera)
# ==============================
def generate_frames():
    global camera

    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' +
                   frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# ==============================
# AUTHENTICATION (BLINK CHECK)
# ==============================
@app.route('/authenticate')
def authenticate():
    global camera

    if camera is None:
        camera = cv2.VideoCapture(0)

    start_time = time.time()
    blink_detected = False

    # Give user 3 seconds to blink
    while time.time() - start_time < 3:
        success, frame = camera.read()

        if not success:
            continue

        if check_face(frame):
            blink_detected = True
            break

    camera.release()     # 👈 VERY IMPORTANT
    camera = None        # 👈 Turns OFF camera light

    if blink_detected:
        token = generate_token()
        return render_template(
            'index.html',
            emotion="Blink Detected",
            token=f"Access Granted! Token: {token}"
        )
    else:
        return render_template(
            'index.html',
            emotion="No Blink Detected",
            token="Access Denied"
        )


# ==============================
# RUN APP
# ==============================
if __name__ == "__main__":
    app.run(debug=True)
