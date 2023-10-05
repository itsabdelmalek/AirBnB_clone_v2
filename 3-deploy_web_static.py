#!/usr/bin/python3
"""
This script creates and distributes an archive to web servers.
"""
import os.path
from datetime import datetime
from fabric.api import *

env.hosts = ["34.232.72.195", "34.229.55.94"]


def do_pack():
    """
    Generates a .tgz archive from the web_static folder.

    Returns:
        str: Archive path if successfully generated, None otherwise.
    """
    d_t = datetime.utcnow()
    file_archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_t.year,
        d_t.month,
        d_t.day,
        d_t.hour,
        d_t.minute,
        d_t.second
    )
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_archive)).failed is True:
        return None
    return file_archive


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive.

    Returns:
        bool: True if successful, False otherwise.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
