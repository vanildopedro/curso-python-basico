#!/bin/python

user_login = {"username":input("username: ")}

if user_login["username"] == "admin":
    print ("Welcome user", user_login["username"])

else:
    print ("Wrong User!")
