#!/usr/bin/env python
#coding=utf8

import sys
import os
import redis

class GetRedisStatus():
    def __init__(self):
        self.val = {}
    def check(self):
        try:
            self.redis = redis.Redis('192.168.1.217', port=6379, password=None)
        except:
            raise Exception, 'Plugin needs the redis module'

    def extract(self, key):
        info = self.redis.info()
        try:
            if key in info:
                self.val[key] = info[key]
            return self.val[key]
        except:
            raise Exception, 'ERROR info not include this key!'

def main():
    if len(sys.argv) == 1:
        print "ERROR! Please enter a key"
    elif len(sys.argv) == 2:
        key = sys.argv[1]
        a = GetRedisStatus()
        a.check()
        print a.extract(key)

if __name__ == "__main__":
    main()
