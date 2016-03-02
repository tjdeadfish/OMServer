#!/usr/bin/python

from fabric.api import *


def local_task():
    local("echo hello")


def mysql_task(download_path, target_path):
    with cd("/home"):
        run("bash test.sh %s %s" % (download_path, target_path))
