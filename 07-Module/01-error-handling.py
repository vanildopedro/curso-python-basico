#!/bin/python


import requests, sys

try:
    user_input = requests.get(input("URL: "))
    #google = requests.get("https://google.com")


except Exception as error:
    print ("Erro nesta linha", type(error).__name__)
    sys.exit()

except KeyboardInterrupt:
    print ("\nExiting the program.")
    sys.exit()

if user_input.status_code == 200:
    print ("Bem-vindo ao site da Google")
