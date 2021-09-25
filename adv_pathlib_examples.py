#!/usr/bin/python

from pathlib import Path

mydir = Path(".").absolute()

mydir.mkdir(parents=True, exist_ok=True)              


newDir = mydir / 'library'

newDir.mkdir(parents=True)
