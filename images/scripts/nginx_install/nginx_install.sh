#!/bin/bash

DOWNLOAD_PATH=$1
TARGET_PATH=$2
SOFT_VERSION=$3

if [ -d ${TARGET_PATH} ];then
        echo "nginx directory is exist."
else
        if [ ! `ls ./nginx-${SOFT_VERSION}.tar.gz` ];then
                wget http://nginx.org/download/nginx-${SOFT_VERSION}.tar.gz -O ${DOWNLOAD_PATH}/nginx-${SOFT_VERSION}.tar.gz
        fi
	cd ${DOWNLOAD_PATH}
        tar zxvf nginx-${SOFT_VERSION}.tar.gz
        cd nginx-${SOFT_VERSION}
        echo "install nginx ..."
        ./configure --prefix=${TARGET_PATH} --user=nobody \
        --group=nobody --with-ld-opt=-ljemalloc --with-http_ssl_module \
        --with-http_addition_module --with-http_sub_module --with-http_dav_module \
        --with-http_flv_module --with-http_gzip_static_module --with-http_stub_status_module \
        --with-http_perl_module --with-mail --with-mail_ssl_module --with-http_geoip_module \
        --with-http_realip_module

        if [ "$?" -eq 0 ];then
                make && make install
        else
                exit 1
        fi
        cp ../nginx_install/init.d/nginx /etc/init.d/nginx
        chmod a+x /etc/init.d/nginx
        mv ${TARGET_PATH}/conf/nginx.conf ${TARGET_PATH}/conf/nginx.conf.old
        cp ../nginx_install/conf/nginx.conf ${TARGET_PATH}/conf
        /bin/cp -rf ../nginx_install/conf/vhosts ${TARGET_PATH}/conf/
        /etc/init.d/nginx start
        chkconfig --add nginx
        chkconfig nginx on
fi
