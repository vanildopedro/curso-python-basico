#!/bin/python

import requests

google = requests.get("https://google.com")

if google.status_code == 200:
    print ("Bem-vindo ao site da Google")
else:
    print ("Site nao encontrado")