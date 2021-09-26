#!/usr/bin/python

from pathlib import Path, PurePath

e_files = Path("./")
print(f'\n Path  iteration { e_files }\n')

d_files = PurePath("./")
print(f'\n PurePath iteration { d_files }\n')

list_files = [l for l in e_files.iterdir() if l.is_file()]
print(f'\n This is a list comprehension with iterdir {list_files}')

d_list_files = [l for l in d_files.iterdir() if l.is_file()]
print(f'\n This is a list comprehension with PurePath iterdir {d_list_files}')

