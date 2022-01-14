#!/usr/bin/python3
# Fabric script that distributes an archive to your web servers
from fabric.api import *
import os
env.hosts = ['35.243.238.95', '3.91.82.101']


def do_deploy(archive_path):
    ''''''
    if os.path.isfile(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    archive = filename.split('.')[0]
    path = "/data/web_static/releases/{}/".format(archive)
    try:
        put("{}".format(archive_path), "/tmp/{}".format(filename))
        run("mkdir -p ".format(path))
        run("tar -xzf /tmp/{} -C {}".format(path))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf {}web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except:
        return False
