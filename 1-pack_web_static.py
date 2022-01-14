#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of
# the web_static folder of your AirBnB Clone repo
from datetime import datetime
from fabric.api import local


def do_pack():
    '''Packing web_static to versions/web_static_datetime.tgz'''
    d = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    namefile = "versions/web_static_{}.tgz".format(d)
    try:
        local("mkdir -p ./versions")
        local("tar -czvf {} web_static".format(namefile))
        return namefile
    except:
        return None
