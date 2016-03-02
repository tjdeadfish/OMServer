import subprocess
import sys
from fabric.api import *


def local_task():
    local("free -m")


def mysql_task():
    with cd("/home"):
        run("bash test.sh")


def process():
    env.hosts = '192.168.1.215'
    env.user = 'root'
    env.password = '?root?'
    env.port = 22

    result = subprocess.call(
        ['fab', '-f', __file__, '-H',  str(env.hosts), '-u', str(env.user), '-p', str(env.password),
         '--port', str(env.port), 'mysql_task']
    )
    #print result
    return result

if __name__ == '__main__':
    # try:
    #     arg = sys.argv[1]
    # except IndexError:
    #     arg = None
    return_val = process()
    print return_val

