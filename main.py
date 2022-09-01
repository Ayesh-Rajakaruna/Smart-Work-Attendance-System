import cv2
from flask import Flask, render_template, Response
import time
from camera import VideoCamera
from imagehadle import saveImage
import os
from PIL import Image
import numpy as np
import io
import random


video_camera = VideoCamera() 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.post('/save')
def save_image():
    frame = video_camera.get_frame()
    image = np.array(Image.open(io.BytesIO(frame)))
    SaveImage = saveImage(image,"1")
    SaveImage.save_image_of_file() 
    return render_template('index.html')

if __name__ == '__main__':
    os.system("start \"\" http://127.0.0.1:5000")
    app.run(port=5000)