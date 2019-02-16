#!\usr\bin\python3
# Abrir o arquivo usuários
#Separar os valores por ","
# Escrever na tela o dicionário 
# {"nome":"Hector","idade":27,"email":"hector.silva@4linux.com.br"


lis = []

for usr in open('usuarios.csv'):
   nome,idade,email = usr.split(',')
   lis.append ({'nome':nome.strip(),'idade' : int(idade.strip()),'email': email.strip()})

for u in sorted(lis, key=lambda n : n['nome']):
    print ('{0:.>20} {1:.>40}' .format (u['nome'], u['email'])  


exit()
meuovo = print
lis = []
def func (n):
    return n['nome']

def fprint(f):
    return (['nome'],['email'])

for usr in open('usuarios.csv'):
   nome,idade,email = usr.split(',')
   lis.append ({'nome':nome.strip(),'idade' : int(idade.strip()),'email': email.strip()})

#for usur in sorted(lis, key=lambda l : l['nome']):
#    meuovo (usur)

for u in sorted(lis, key=lambda n : n['nome']):
    meuovo ('{0:.>20} {1:.>40}' .format (u['nome'], u['email'])  #forma1
#    meuovo ('{0[nome]:.>20} {0[email]:.>40}'.format(u))          #forma2
    
for i in sorted(lis, key=fprint())

    

# resolução com lambda   
# for i in sorted(lis, key=lambda i : i['nome]):
#     meuovo (i,e)

exit ()
# resolução com função
for i in sorted(lis, key=func()):
 meuovo (i)

#           for n.append( in 

exit() #retornar nomes ordernados
nom = []
for u in lis:
    nom.append(u['nome'])

for orde in sorted(nom):
    print(orde)

exit() # imprimir somente nomes   
for u in lis:
    print (u['nome'])


exit()
for user in open('usuarios.csv'):
 nome,idade, email = user.split(',')
 print ({'nome': nome.strip(),'idade' : int(idade.strip()) ,'email' : email.strip()})







exit ()
for user in open ('usuarios.csv'):
    #aqui eu preciso separar por ","
    print (user) 


exit ()
usuarios = open ('usuarios.csv')
print (usuarios)

for user in usuarios:
    if usr in user.split(','):
        print (usr)

