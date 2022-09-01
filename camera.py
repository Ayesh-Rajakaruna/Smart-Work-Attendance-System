import cv2
import time
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.vid = cv2.VideoCapture(0)
        time.sleep(2.0)

    def __del__(self):
        self.vid.release()

    def get_frame(self):
        ret, frame = self.vid.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
