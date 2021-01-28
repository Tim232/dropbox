import os
import datetime

class Dropbox:
    def __init__(self, token):
        self.token = token
        print(self.token)
        if not os.path.isdir('dropboxFiles'):
            os.mkdir('dropboxFiles')

    def files_upload(self, file:bytes, name:str):
        now = f'dropboxFiles/{datetime.datetime.now().strftime("%Y%m%d%H")}'
        if not os.path.isdir(now):
            os.mkdir(now)
        with open(f"{now}/{name}", 'wb') as f:
            f.write(file)
