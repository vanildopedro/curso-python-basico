#!/bin/python

import os

dirc = os.getcwd()
print ("Meu directorio actual", dirc)

ficheiros = os.listdir('.')

for f in ficheiros:
    print(f)