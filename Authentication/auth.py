from googleapiclient.discovery import build

class Auth:
    def __init__(self, keyAuth = 'AIzaSyCTY4ExbPCJrOH-1tOSAZr_6cbiyJzU6iw'):
        #key 1: AIzaSyCTY4ExbPCJrOH-1tOSAZr_6cbiyJzU6iw
        #key 2: AIzaSyA33m-lnUKd5bHdVm7Kvjw2C-GenJMpja4
        self.__SERVICE_NAME = 'youtube'
        self.__SERVICE_VERSION = 'v3'
        self.keyAuth = keyAuth
        self.logged = False

    
    def loginYoutube(self) :
        self.service = build(self.__SERVICE_NAME, self.__SERVICE_VERSION, developerKey=self.keyAuth)
        return self.service