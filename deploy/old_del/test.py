#!/usr/bin/env python
#coding=utf8

import subprocess
import sys
import os


jps = '/usr/bin/jps'
jstat = '/usr/bin/jstat'
class Jprocess:
    """Check java process presence and get memory status"""
    def __init__(self, arg):
        """Initialize defalut values"""
        self.pdict = {
        "jpname": arg,
        "pid": 0,
        }

        self.zdict = {
        "heap_used" : 0,
        "heap_max" : 0,
        "perm_used" : 0,
        "perm_max"  : 0,
        }

    def get_pid(self):
        """Check if java process is running / Get it's pid"""
        jpsout = subprocess.Popen(['sudo', jps], stdout=subprocess.PIPE)

        for line in jpsout.stdout:
            line = line.rstrip('\n')
            pid, name = line.split(' ', 1)
            if  name == self.pdict['jpname']:
                self.pdict['pid'] = pid
        #print self.pdict['pid']

    def get_jstats(self):
        """Check if java process is running"""
        self.pdict.update(self.fill_jstats("-gc"))
        self.pdict.update(self.fill_jstats("-gccapacity"))
        #print self.pdict


    def fill_jstats(self, ops):
        """Return a dictionary with jstat values"""
        jstatout = subprocess.Popen(['sudo', jstat, ops, str(self.pdict['pid'])], stdout=subprocess.PIPE)
        stdout, stderr = jstatout.communicate()
        legend, data = stdout.split('\n', 1)
        mydict = dict(zip(legend.split(), data.split()))
        return mydict

    def compute_jstats(self):
        """Compute stats not given directly by jstat"""
        self.zdict['perm_used'] = round(float(self.pdict['PU']) * 1024,2)
        self.zdict['perm_max'] = round(float(self.pdict['PGCMX']) * 1024,2)
        self.zdict['heap_used'] = round(((float(self.pdict['EU']) + float(self.pdict['OU'])) * 1024),2)
        self.zdict['heap_max'] = round(((float(self.pdict['NGCMX']) + float(self.pdict['OGCMX'])) * 1024),2)

    def get_value(self, key):
        return self.zdict[key]

def useage():
    """Display program useage"""
    print "nUsage : ", sys.argv[0], "process_name key"
    print "process_name: java process name as seen in jps outputn"
    sys.exit(1)


def main():
    key_list = ['perm_used', 'perm_max', 'heap_used', 'heap_max']
    if len(sys.argv) == 3 and sys.argv[2] in key_list:
        jpname = sys.argv[1]
        key = sys.argv[2]
        a = Jprocess(jpname)
        a.get_pid()
        a.get_jstats()
        a.compute_jstats()
        print a.get_value(key)
    else:
        useage()

if __name__ == "__main__":
    main()
