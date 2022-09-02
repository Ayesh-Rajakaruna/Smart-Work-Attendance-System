import cv2
from flask import Flask, render_template, Response
import time
from camera import VideoCamera
from get_photo_of_employers import get_photo_of_employers
from facedetection import facedetection
from uplodetofirebae import uplodetofirebae
import os
from PIL import Image
import numpy as np
import io
import random


video_camera = VideoCamera() 

app = Flask(__name__)

@app.get('/')
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

@app.post('/save') # Get poto and save this in the file
def save_image():
    frame = video_camera.get_frame()
    image = np.array(Image.open(io.BytesIO(frame)))
    get_poto = get_photo_of_employers(image) 
    get_poto.save_image_in_the_file() 
    return render_template('index.html')

@app.post('/submit')
def submit():
    face_detection = facedetection() #Go to the file and all image crop to face
    face_detection.cropallfasce()
    firebace = uplodetofirebae("1") #Uplode to firebace
    firebace.uplodePoto()
    face_detection.deleteallfile() #Delete all file
    return render_template('index.html')

if __name__ == '__main__':
    os.system("start \"\" http://127.0.0.1:5000")
    app.run(port=5000)