#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static folder
"""
from fabric.api import local, task, run, env, put
from datetime import datetime
import os
env.user = "ubuntu"
env.hosts = ['54.172.230.228', '54.87.240.48']


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


def do_deploy(archive_path):
    """doc"""
    file = archive_path.split('/')[-1].split('.')[0]
    if not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp/')
    run(f'mkdir -p /data/web_static/releases/{file}/')
    run(f'tar -xzf /tmp/{file}.tgz -C \
    /data/web_static/releases/{file}/')
    run(f'rm /tmp/{file}.tgz')
    run(f'mv /data/web_static/releases/{file}/web_static/* \
    /data/web_static/releases/{file}/')
    run(f'rm -rf /data/web_static/releases/{file}/web_static')
    run('rm -rf /data/web_static/current')
    run(f'ln -s /data/web_static/releases/{file}/ \
    /data/web_static/current')
    print('New version deployed!')
    return True
