#!/usr/bin/python

# import subprocess
from pathlib import Path

myfile = Path('.').absolute()
print(f'\n{myfile} is the absolute path\n')

myfile1 = Path('.').absolute().as_uri()
print(f'\n{myfile1} is the uri path\n')

myfile2 = Path('.').absolute().as_posix()
print(f'\n{myfile2} is the posix path\n')

pdir = myfile.parent
print(f'\n{pdir} is the parent directory\n')

rel_pdir = myfile.relative_to(pdir)
print(f'\n{rel_pdir} is the directory relative to parent\n')

ofile = myfile / "pathlib-examples.py"
print(f'\n{ofile} is a new file in the current  directory\n')

exist = ofile.exists()
print(f'\n Does this file exist (True or False)? {exist} ')

chkfile = ofile.is_file()
print(f'\n Is this a file (True or False)? {chkfile} ')

chkdir = pdir.is_dir()
print(f' \n ofile is a {type(ofile)} \n')

print(f'\n Is this a directory? (True or False)? {chkdir} ')
# find all the sub directories in the current directory

list_subdir = [ s for s in pdir.iterdir() if s.is_dir()]
print(f'\n These are the subdir of the given dir {list_subdir}')

list_subdir = [ s for s in myfile.iterdir() if s.is_file()]
print(f'\n These are the files of the given dir {list_subdir}')

list_glob = list(myfile.glob('*.py'))
print(f'\n  List files with the py extension {list_glob}')

list_rglob = list(myfile.rglob('*.py'))
print(f'\n  List all files in the subtree with the py extension {list_rglob}')
