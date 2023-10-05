#!/usr/bin/python3
"""
This script distributes an archive to web servers.
"""

import os
from fabric.decorators import task
from fabric.api import *

env.hosts = ['34.232.72.195', '34.229.55.94']


@task
def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        if not os.path.exists(archive_path):
            print(f"Error: Archive not found at {archive_path}")
            return False

        w_ext = os.path.basename(archive_path)
        wo_ext = os.path.splitext(w_ext)[0]

        put(archive_path, "/tmp")

        run(f"mkdir -p /data/web_static/releases/{wo_ext}")
        run(f"tar -xzf /tmp/{w_ext} -C /data/web_static/releases/{wo_ext}")

        run(f"rm /tmp/{w_ext}")

        run(
            f"mv /data/web_static/releases/{wo_ext}/web_static/* "
            f"/data/web_static/releases/{wo_ext}"
        )
        run(f"rm -rf /data/web_static/releases/{wo_ext}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(
            f"ln -s /data/web_static/releases/{wo_ext}/ "
            f"/data/web_static/current"
        )

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
