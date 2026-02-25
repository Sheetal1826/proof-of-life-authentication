# AI Proof of Life Authentication System

This project is a real-time liveness detection system which verifies whether the user is physically present using blink detection through webcam input.

The system helps in preventing spoofing attacks using photos or videos by checking if the user performs a live blink action.

---

## Features

- Real-time Face Detection  
- Blink Detection using MediaPipe  
- Liveness Verification  
- Secure Token Generation  
- Anti-Spoofing Mechanism  
- Flask-based Web Application  
- Live Camera Feed Interface  

---

## Tech Stack

- Python  
- Flask  
- OpenCV  
- MediaPipe  
- NumPy  
- HTML  
- CSS  

---

## Project Structure

```
proof-of-life-authentication/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── liveness.py
├── emotion.py
├── auth_token.py
├── requirements.txt
└── .gitignore
```

## Working

1. User opens the web application.
2. Webcam starts capturing live video.
3. System detects facial landmarks.
4. User is asked to blink.
5. Blink Detection algorithm verifies liveness.
6. If verified:
   - Access Granted
   - Authentication Token Generated
7. Otherwise:
   - Access Denied
Note: Emotion-based detection was initially implemented, 
but later replaced with blink-based liveness detection 
to enhance security and prevent spoofing attacks.

---

## Demo

This project runs locally using Flask.  
To test the application:

1. Run `python app.py`
2. Open `http://127.0.0.1:5000`
3. Blink once to verify liveness
4. A secure authentication token will be generated

---

## Future Scope

- Face Recognition Integration  
- Multi-factor Authentication  
- Head Movement Detection  
- Deployment using Cloud  

---

## Author

Sheetal  
Aspiring Full Stack Developer  
[GitHub Profile](https://github.com/Sheetal1826)
