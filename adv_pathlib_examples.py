#!/usr/bin/python

from pathlib import Path

mydir = Path(".").absolute()

mydir.mkdir(parents=True, exist_ok=True)              



# newDir = mydir / 'library'

# newDir.mkdir(parents=True)

print("View code that makes directories with mkdir ")

nfile = Path('./library') / "newfile.txt"

nfile.exists()

print(nfile.exists)

# nfile.mkdir(parents=True,exist_ok=True)

nfile.write_text('Hello Kirk Tollive')

print( "Wrote file and file content with file write_File")

read_file = nfile.read_text()

print(f"Read file info with read_text {read_file}")
