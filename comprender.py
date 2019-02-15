
#!/usr/bin/python3
meuovo = print
for n in map(lambda a : a*2,[1,2,3,4]):
 meuovo (n)



exit()
duck_tails =['Huguinho|1', 'Zezinho|2', 'Luizinho|3']

#percorrer a variável e exibir apenas os nomes, sem os numeros

for d in [k.split('|')[0] for k in duck_tails]:
# pode incluir no for  if 'Zezinho' not in k]:
#    print (d[0],d[-1])
    if 'Zezinho' not in d:
     print (d)

    
