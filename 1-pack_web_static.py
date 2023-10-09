#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from 
the contents of the web_static folder
"""
from fabric.api import local, task
from datetime import datetime


def do_pack():
    """pack web_static folder"""
    try:
        cur_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
        archive = f"web_static_{cur_datetime}.tgz"
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(archive))
        return f"versions/{archive}"
    except Exception:
        return None
