#!/usr/bin/env python
#coding=utf8

import time
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
from Crypto.PublicKey.pubkey import *
import sys


env.user = 'root'
env.password = '?root?'
env.port = 22
env.hosts = '192.168.1.215'


@runs_once
def local_task():
    local("free -m")

def remote_task():
    with cd("/home"):
        run("bash test.sh")





if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = do_something(arg)