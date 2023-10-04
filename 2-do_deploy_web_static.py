#!/usr/bin/python3
"""
This Fabric script distributes an archive to your web servers.
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['34.232.72.195', '34.229.55.94']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.

    Args:
        archive_path (str): Path to the archive.

    Returns:
        bool: True if all operations have been done correctly, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split('/')[-1]
        file_name_no_ext = file_name.split('.')[0]
        release_path = "/data/web_static/releases/{}".format(file_name_no_ext)

        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        return True

    except Exception as e:
        print(e)
        return False
