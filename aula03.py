

#!/usr/bin/python3

#arquivo = open ('zen.txt').read().upper()

arquivo = open ('zen.txt')

#print (linha, end='')

#mod -> 1 % 2 -> Se é par ou impar
# if 'belzebu' inn demonios:
# Printar apenas as linhas com palavras, ignorando as linhas com "-"

for i, linha in enumerate(arquivo):
    if i % 2 == 0;
      print (linha.strip())

exit () # forma 2
i = 0
for linha in arquivo:
    linha = linha.strip()
     if i % 2 == 0:
         print (linha)
         i = i + 1

exit () #forma 1 
for linha in arquivo:
    if '-\n'   not in linha:
       print (linha)


    
