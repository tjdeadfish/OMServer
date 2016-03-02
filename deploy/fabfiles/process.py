import subprocess
import sys

def process(vals):
    p_hosts = str(vals['server_external_ip'])
    p_user = str(vals['server_admin'])
    p_passwd = str(vals['server_password'])
    p_port = str(vals['server_port'])

    # SHELL_CMD = "fab -f /Users/jack/PycharmProjects/OMServer/deploy/fabfiles/tasks.py %s mysql_task" % vals
    # process = subprocess.Popen(SHELL_CMD, shell=True, stdout=subprocess.PIPE)
    # stdout, stderr = process.communicate()
    # return stdout
    task_process = subprocess.call(['fab', '-f', '/Users/jack/PycharmProjects/OMServer/deploy/fabfiles/tasks.py',
                                     p_hosts, p_user, p_passwd, p_port, 'mysql_task'], shell=True)

    print task_process

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = process(arg)
    print return_val