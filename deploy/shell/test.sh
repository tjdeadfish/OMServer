#!/bin/base

download_path=$1
target_path=$2
       
if [ ! -d ${target_path}/mysql ];then
	echo "download mysql ..."
	if [ ! -f ${download_path}/mysql-5.6.26.tar.gz ];then
		cd ${download_path}
		wget http://dev.mysql.com/get/Downloads/MySQL-5.6/mysql-5.6.26.tar.gz
	fi
	if [ $? -eq 0 ];then
		echo "download complete."
	else
		echo "download faild"
		exit 1
	fi

	tar zxf mysql-5.6.26.tar.gz
	cd mysql-5.6.26
	cmake \
		-DCMAKE_INSTALL_PREFIX=/data/lnmp/mysql \
		-DMYSQL_DATADIR=/data/lnmp/mysql/var \
		-DSYSCONFDIR=/etc \
		-DMYSQL_UNIX_ADDR=/tmp/mysql.sock \
		-DMYSQL_TCP_PORT=3306 \
		-DDEFAULT_CHARSET=utf8 \
		-DDEFAULT_COLLATION=utf8_general_ci \
		-DEXTRA_CHARSETS=all
	if [ "$?" -eq 0 ];then
		make && make install
	fi

	if [ ! `cat /etc/group | awk -F: '{print $1}'| grep mysql` ];then
		groupadd mysql
	fi
	if [ ! `cat /etc/passwd | awk -F: '{print $1}'| grep mysql` ];then
		useradd -M -g mysql -s /sbin/nologin mysql
	fi

	cp ../profile.d/mysql.sh /etc/profile.d/
	echo "/data/lnmp/mysql/lib" > /etc/ld.so.conf.d/mysql.conf
	ldconfig
	source /etc/profile.d/mysql.sh
	echo
	echo "init ..."
	echo
	mkdir /data/lnmp/mysql/var
	chown -R mysql:mysql /data/lnmp/mysql/var
	if [ -f /etc/my.cnf ];then
		rm -rf /etc/my.cnf
	fi
	/data/lnmp/mysql/scripts/mysql_install_db --user=mysql --basedir=/data/lnmp/mysql --datadir=/data/lnmp/mysql/var --explicit_defaults_for_times
	if [ "$?" -eq 0 ];then
		echo "init success."
	else
		exit 1
	fi
	cp  support-files/mysql.server  /etc/rc.d/init.d/mysqld
	cp ../conf/my.cnf /etc/
	chmod a+x /etc/rc.d/init.d/mysqld
	mkdir /data/lnmp/mysql_binlog
	mkdir /data/lnmp/mysql/logs
	chown -R mysql.mysql /data/lnmp/mysql/logs
	chown -R mysql.mysql /data/lnmp/mysql_binlog
	/etc/init.d/mysqld start
	chkconfig --add mysqld
	chkconfig mysqld on
else
		echo "mysql directory is exist. will be quit"
		exit 0
fi
