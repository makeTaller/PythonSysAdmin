#!/usr/bin/python

import subprocess
# import os

# p = os.system("ls")

newE = subprocess.run("ls")
print(f'\nSubprocess regular {newE}\n')

newp = subprocess.run(["ls"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(f'\nSubprocess with stdout and stderr {newp}\n')

newG = subprocess.run("ls", capture_output=True)
print(f'\nSubprocess with capture output true {newG}\n')

newS = subprocess.run("ss -lntu", shell=True)
# Huge security flaw!!!!!
print(f'\nSubprocess with shell true {newS}\n')

userinput = "a.txt; pwd"
command = "cat {}".format(userinput)

newSt = subprocess.run(command, shell=True, capture_output=True)
print(f"\nSubprocess example of the security flaw {newSt}")


# p = subprocess()
