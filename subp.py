#!/usr/bin/python

import subprocess
# import os

# p = os.system("ls")

newp = subprocess.run(["ls","-la"],stdout=subprocess.PIPE)

print(newp)

# p = subprocess()
