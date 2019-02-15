#!\usr\bin\python3
# Abrir o arquivo usuários
#Separar os valores por ","
# Escrever na tela o dicionário 
# {"nome":"Hector","idade":27,"email":"hector.silva@4linux.com.br"}

meuovo = print
lis = []
def func (i):
    return i['nome']

for usr in open('usuarios.csv'):
   nome,idade,email = usr.split(',')
   lis.append ({'nome':nome.strip(),
       'idade' : int(idade.strip()),
       'email': email.strip()})
# resolução com lambda   
#   for i in sorted(lis, key=lambda i : i['nome']):
#     meuovo (i)

# resolução com função
for i in sorted(lis, key=func):
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

