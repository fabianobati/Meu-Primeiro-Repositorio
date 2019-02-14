#!\usr\bin\python3
# Abrir o arquivo usuários
#Separar os valores por ","
# Escrever na tela o dicionário 
# {"nome":"Hector","idade":27,"email":"hector.silva@4linux.com.br"}

for user in open('usuarios.csv'):
 nome,idade, email = user.split(',')
 print ({'nome': nome.strip(),
         'idade' : int(idade.strip()) ,
          'email' : email.strip()})

exit()
ide==int(idade)






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

