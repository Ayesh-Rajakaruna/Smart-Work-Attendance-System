from firebase_admin import credentials, initialize_app, storage
import os

class uplodetofirebae:
    def __init__(self, workid, folderName = 'photo_of_employers', localpath=".\\static\\photo_of_new_employer"):
        self.workid = workid
        self.folderName = folderName
        self.localpath = localpath
        self.cred = credentials.Certificate(".\\firebase_configuration\\config.json")
        try:
            initialize_app(self.cred, {'storageBucket': 'smart-work-attendance-system.appspot.com'})
            print("initialize the app")
        except:
            print("Can't initialize the app")
        self.path = "{}//{}".format(self.folderName, self.workid)
        self.dir_list = os.listdir(self.localpath)
    def makefilepath(self):
        path_lis = []
        for imgname in self.dir_list:
            path_local = "{}\\{}".format(self.localpath, imgname)
            path_firebase = "{}/{}/{}".format(self.folderName,self.workid,imgname)
            path_lis.append((path_local,path_firebase))
        return path_lis
    def uplodePoto(self):
        path_lis = self.makefilepath()
        bucket = storage.bucket()
        for path in path_lis:
            path_local, path_firebase = path
            blob = bucket.blob(path_firebase)
            blob.upload_from_filename(path_local)

