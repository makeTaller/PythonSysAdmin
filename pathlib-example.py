#!/usr/bin/python

# import subprocess
from pathlib import Path

myfile = Path('.').absolute()

myfile1 = Path('.').absolute().as_uri()

myfile2 = Path('.').absolute().as_posix()

pdir = myfile.parent

rel_pdir = myfile.relative_to(pdir)

ofile = myfile / "pathlib-examples.py"

exist = ofile.exists()

chkfile = ofile.is_file()

chkdir = pdir.is_dir()

print(f'\n{myfile} is the absolute path\n')

print(f'\n{myfile1} is the uri path\n')

print(f'\n{myfile2} is the posix path\n')

print(f'\n{pdir} is the parent directory\n')

print(f'\n{rel_pdir} is the directory relative to parent\n')

print(f'\n{ofile} is a new file in the current  directory\n')

print(f'\n Does this file exist (True or False)? {exist} ')

print(f'\n Is this a file (True or False)? {chkfile} ')

print(f' \n ofile is a {type(ofile)} \n')

print(f'\n Is this a directory? (True or False)? {chkdir} ')

