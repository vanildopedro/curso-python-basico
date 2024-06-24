#!/bin/python

#“r” - Read - Valor por defeito. Abre um ficheiro para leitura, dá erro se o ficheiro não existir
#“a” - Append - Abre um ficheiro para adicionar conteúdo, cria o ficheiro se este não existir
#“w” - Write - Abre um ficheiro para escrita, cria o ficheiro se este não existir
#“x” - Create - Cria o ficheiro especificado, dá um erro se o ficheiro existir

ficheiro_read = open("myfile.txt") #"r"

print (ficheiro_read.read())

#Create new file
ficheiro_create = open("myfile_create2.txt", "x")

#Write file
ficheiro_write = open("myfile_write.txt", "w")
ficheiro_write.write("Bem-vindo ao meu primeiro programa de leitura de ficheiro. Modo-Write")
ficheiro_write.close()

ficheiro_write = open("myfile_write.txt")
print (ficheiro_write.read())

#Append file
ficheiro_write = open("myfile_append.txt", "a")
ficheiro_write.write("\nBem-vindo ao meu primeiro programa de leitura de ficheiro. Modo-Append 3")
ficheiro_write.close()

ficheiro_write = open("myfile_append.txt")
print (ficheiro_write.read())