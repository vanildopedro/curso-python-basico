#!/bin/python

#As listas são utilizadas para armazenar vários itens numa única variável.

Carros = ["Toyota",22,"BMW",True,"Mazda","Honda"]

print(len(Carros),Carros)
print(type(Carros))

print(Carros[1])
print(Carros[-2])

print(Carros[1:5])

Carros.append("Nissan")

print(Carros)