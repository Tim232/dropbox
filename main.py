import os
import datetime

class Dropbox:
    def __init__(self, token):
        self.token = token
        print(self.token)

    def files_upload(self, file:bytes, name:str):
        if not os.path.isdir('dropboxFiles'):
            os.mkdir('dropboxFiles')
        now = 'dropboxFiles/'+str(datetime.datetime.now().strftime("%Y%m%d%H"))
        if not os.path.isdir(now):
            os.mkdir(now)
        name = now+"/"+name
        with open(name, 'wb') as f:
            f.write(file)
