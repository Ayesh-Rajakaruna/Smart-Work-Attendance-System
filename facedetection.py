import cv2
import time
import numpy as np
import os

class facedetection():
    def __init__(self, localpath=".\\static\\photo_of_new_employer"):
        self.localpath = localpath
        self.dir_list = os.listdir(self.localpath)
        self.classifier = "models\\facial_recognition_model.xml"
        self.face_cascade = cv2.CascadeClassifier(self.classifier)
        self.lis = self.localpath.split('\\')[1:]
    def get_face(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces)>0:
            (x,y,w,h) = faces[0]
            face_image = image[y:y+h, x:x+w]
            resize_image = cv2.resize(face_image, (124, 124), interpolation = cv2.INTER_AREA)
            return face_image
        else:
            return "No"
    def cropallfasce(self):
        for imgname in self.dir_list:
            path = "{}//{}".format(self.localpath,imgname)
            img = cv2.imread(path)
            img = self.get_face(img)
            try:
                cv2.imwrite(path, img)
            except:
                os.remove(path)
    def deleteallfile(self):
        file_list = os.listdir(self.localpath)
        for imgefile in file_list:
            path = "{}//{}".format(self.localpath,imgefile)
            os.remove(path)
    def counfile(self):
        count = 0
        for root_dir, cur_dir, files in os.walk(r'{}\\{}'.format(self.lis[0],self.lis[1])): 
            count += len(files)
        return count
                