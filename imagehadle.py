import cv2
import time
import numpy as np
import os

class saveImage():
    def __init__(self, img, workid, folderName="static"):
        self.image = img
        self.folderName = folderName
        self.workid = workid
        self.classifier = "models\\facial_recognition_model.xml"
    def makefolder(self):
        if not ".\\{}".format(self.folderName) in [x[0] for x in os.walk(".")]:
            os.mkdir("{}".format(self.folderName))
        if not "{}\\{}".format(self.folderName,self.workid) in [x[0] for x in os.walk("{}".format(self.folderName))]:
            os.mkdir("{}\\{}".format(self.folderName,self.workid))
    def counfile(self):
        count = 0
        for root_dir, cur_dir, files in os.walk(r'{}\\{}'.format(self.folderName,self.workid)): 
            count += len(files)
        return count
    def get_face(self,image):
        haar_cascade = cv2.CascadeClassifier(self.classifier)
        image=cv2.flip(image,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = haar_cascade.detectMultiScale(mini)

    def save_image_of_file(self):
        self.makefolder()
        count = self.counfile()
        cv2.imwrite("{}\\{}\\{}.jpg".format(self.folderName,self.workid,count+1), self.image)