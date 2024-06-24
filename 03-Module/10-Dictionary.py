#!/bin/python

#Os dicionários são utilizados para armazenar valores de dados em pares "Key:Value".

Carros = {"Toyota":"Vitz","Toyota_1":"MarkX","Toyota_2":"Fortuner"}

#print(type(Carros),Carros)

print(Carros)

print(Carros["Toyota_1"])

VarGet = Carros.get("Toyota_2")

print(VarGet)