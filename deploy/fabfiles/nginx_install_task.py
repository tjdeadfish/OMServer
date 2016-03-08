#!/usr/bin/python

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm


# @task
# @runs_once
# def tar_task(local_bash_path, local_bash_name, fabric_task):
#     with lcd("%s" % local_bash_path):
#         local("zip -r %s %s.sh init.d conf" % (local_bash_name, fabric_task))


@task
@runs_once
def put_script(local_bash_path, local_bash_name, download_path, fabric_task):
    run('mkdir -p %s' % download_path)
    print "create %s directory success." % download_path
    with settings(warn_only=True):
        with cd('%s' % download_path):
            run('rm -rf %s' % fabric_task)
            result = put('%s/%s' % (local_bash_path, local_bash_name),  '%s' % download_path)
            if result.failed and not confirm("put file failed, Continue[Y/N]"):
                abort("Aborting file put job!")
            print green("put ...OK!")


@task
def extract_script(download_path, local_bash_name):
    with cd('%s' % download_path):
        result = run("unzip %s" % local_bash_name)
        if result.failed:
            abort("extract failed")
        print green("extract success.")


@task
def install_dep(download_path):
    with cd('%s' % download_path):
        result = run('yum install -y epel-release vim unzip wget gcc '
                     'gcc-c++ jemalloc jemalloc-devel pcre pcre-devel openssl '
                     'openssl-devel perl perl-ExtUtils-Embed geoip geoip-devel')
        if result.failed:
            abort("dep install failed.")
        print "dep install success."


@task
def nginx_install_task(download_path, target_path, soft_version, fabric_task):
    with cd("%s/%s" % (download_path, fabric_task)):
        run("bash -x %s.sh %s %s %s" % (fabric_task, download_path, target_path, soft_version))


@task
def nginx_install(download_path, target_path, soft_version, local_bash_path, local_bash_name, fabric_task):
    # tar_task(local_bash_path, local_bash_name, fabric_task)
    install_dep(download_path)
    put_script(local_bash_path, local_bash_name, download_path, fabric_task)
    extract_script(download_path, local_bash_name)
    nginx_install_task(download_path, target_path, soft_version, fabric_task)

