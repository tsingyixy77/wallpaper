#!/bin/env python2

from unsplash.api import Api
from unsplash.auth import Auth
import urllib2
import os

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

file = urllib2.urlopen(url)
download_path = '/home/hutan/Pictures/Wallpapers/'
pic_path = download_path + pic_id
with open(pic_path, 'wb') as code:
    code.write(file.read())
command = 'gsettings set org.gnome.desktop.background picture-uri ' + pic_path
os.system(command)

