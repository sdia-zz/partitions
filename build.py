#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, os, subprocess


if __name__ == '__main__':
    try:
        f_path = sys.argv[1]
        f_name = f_path.split('/')[-1]
        f_abspath = os.path.abspath(f_path)

    except Exception, e:
        print './build /path/to/myfile.ly' 
        print e
        exit(1)

    shell_command = "lilypond -o build/ {}".format(f_abspath)
    print shell_command
    # exit()

    r = subprocess.call(["/home/sdia/bin/lilypond -o /home/sdia/src/partitions/build/ {}".format(f_abspath)])
    print r
