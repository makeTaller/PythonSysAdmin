#!/usr/bin/python

import subprocess
import shlex
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

shq = shlex.quote(userinput)
command1 = "cat {}".format(shlex.quote(userinput))
print( command1)

# This is how to make a list of a command of text

commandNew = shlex.split("cat 'xyc fer' >> file.txt")
print(f'This is a list of commmands created by shlex.split {commandNew}')

# file_input = subprocess.run(["python test.py"], capture_output=True, input="abc\ndef", text=True)
# print(f'This is putting input from user commands into the test.py {file_input}')

# file_input = subprocess.run(["python test.py"], capture_output=True, stdin=open("abc\ndef", "r", text=True)

# this is to make the shell sleep 
subprocess.run(["sleep","3"], timeout=5)

try:
    subprocess.run(["ls","-xla"], check=True)
except subprocess.CalledProcessError:
    print("failed")


# p = subprocess()
