#!/usr/bin/env python
# coding=utf-8
import os
import sys
import re

OUT_FILE = "./code_export.out"

re_comp = re.compile(r'(.*\.py$|.*\.js|.*\.css|.*\.html|.*\.cpp|.*\.h)')


def filter_out(file_name):
    filter_list = ['bower_component', 'node_modules', 'ionic', 'lib']
    for fil in filter_list:
        if fil in file_name:
            return True
    return False


def main(abs_path):
    files = os.listdir(abs_path)
    while len(files) > 0:
        current = os.path.join(abs_path, files.pop())

        if os.path.isdir(current):
            main(current)

        if not re_comp.match(current) or filter_out(current):
            continue

        elif os.path.isfile(current):
            with open(OUT_FILE, "a") as fo:
                fin = open(current, "r")
		ch_end = current.split('.')[-1]
		if ch_end=="py": 
                    fo.write("\n'''\nfile: \n%s\n'''\n" % current)
		elif ch_end=="html":
                    fo.write("\n<!--\nfile: \n%s\n-->\n" % current)
		else:
		    fo.write("\n/*\nfile: \n%s\n*/\n" % current)
		line = fin.readline()
		while line!='':
		    while line=="\n":
			line = fin.readline()
		        pass
                    fo.write(line)
		    line = fin.readline()


if __name__ == '__main__':
    path = sys.argv[1]
    OUT_FILE = sys.argv[2]
    os.system("echo > %s" % OUT_FILE)
    main(path)
