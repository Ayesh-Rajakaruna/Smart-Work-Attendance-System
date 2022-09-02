import cv2
import time
import numpy as np
import os

class get_photo_of_employers():
    def __init__(self, img, localpath=".\\static\\photo_of_new_employer"):
        self.image = img
        self.localpath = localpath
        print(self.localpath)
        print(self.localpath.split('\\'))
        self.lis = self.localpath.split('\\')[1:]
    def makefolder(self):
        if not ".\\{}".format(self.lis[0]) in [x[0] for x in os.walk(".")]:
            os.mkdir("{}".format(self.lis[0]))
        if not "{}\\{}".format(self.lis[0],self.lis[1]) in [x[0] for x in os.walk("{}".format(self.lis[0]))]:
            os.mkdir("{}\\{}".format(self.lis[0],self.lis[1]))
    def counfile(self):
        count = 0
        for root_dir, cur_dir, files in os.walk(r'{}\\{}'.format(self.lis[0],self.lis[1])): 
            count += len(files)
        return count
    def save_image_in_the_file(self):
        self.makefolder()
        count = self.counfile()
        cv2.imwrite("{}\\{}\\{}.jpg".format(self.lis[0], self.lis[1], count+1), self.image)