from fabric.api import env, run

def main():
    run("uname -a")

def setup():
    env.host_string = "root@192.168.1.215"

if __name__ == '__main__':
    setup()
    main()
