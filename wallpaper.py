#!/mingw32/bin/python3
#! -*- coding: utf-8 -*-

from unsplash.api import Api
from unsplash.auth import Auth
import requests
import os
import platform

is_linux = True if platform.system() == 'Linux' else False
client_id='1e0dc51c119091d5eb19bc72da7de7abfe9c2b090129cbb3deb736bb99f28218'
client_secret='2600e4830347cd34a14561ad79dd1098bf5bb0aa59823bfb4585997dc3ac39af'
redirect_uri="urn:ietf:wg:oauth:2.0:oob"

auth = Auth(client_id, client_secret, redirect_uri)
api = Api(auth)

width = 3840
height = 2160

random_pic = api.photo.random(w=width, h=height)
pic_id = random_pic[0].id
url = api.photo.download(pic_id).get('url')

download_path = 'D:\Pictures\\' if not is_linux else '/home/hutan/Pictures/Wallpapers/'
pic_path = download_path + pic_id + '.jpg'
print('downloading ' + url)
rr = requests.get(url)
with open(pic_path, 'wb') as ff:
    ff.write(rr.content)
print('done, begin to set')
if not is_linux:
    import ctypes
    h = ctypes.windll.LoadLibrary('C:\\Windows\\System32\\user32.dll')
    h.SystemParametersInfoW(20, True, pic_path, 1)
else:
    command = 'gsettings set org.gnome.desktop.background picture-uri ' + pic_path
    os.system(command)
#with open(pic_path, 'wb') as code:
#    code.write(file.read())

