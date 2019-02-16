
#!/usr/bin/python3

def hprint ():
    print ('{0:.<4}{1:.>20} {2:.>40}'.format('ID','NOME', 'EMAIL'))

def fprint(i, user):
    print ('{0:.>4} {1:.<20}{2:.>40}'.format(i,user['nome'],user['email']))

lis = []
for usr in open('usuarios.csv'):
   nome,idade,email = usr.split(',')
   lis.append ({'nome':nome.strip(),'idade' : int(idade.strip()),'email': email.strip()})

hprint()
for i, u in enumerate(sorted(lis, key=lambda n : n['nome']), start=1): #sem definir função
#    print ('{0:.>20} {1:.>40}' .format (u['nome'], u['email']),i)
       fprint(i,u)

