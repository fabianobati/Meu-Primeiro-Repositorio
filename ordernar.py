#!/usr/bin/python3

#letras = ['a','Z','d','h','l','p','i','n','t','o','a']
letras = ['a','Z','b','c','A']
#ordernar as letras e escreve-las em maius

#for i in sorted(letras):
#  print (i)

#criar uma função que recebe um valor qualquer e retorna essa letra em maius
def mar (letras):
    return letras.upper()

#ordernadas = sorted(letras, key=mar)
ordenadas = sorted(letras, key=lambda i : i.upper())

for l in ordenadas:
    print (l)




