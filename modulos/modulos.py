import time, random  # pode se importar todos os módulos na mesma linha separados por vírgula
from subprocess import run, PIPE
from datetime import datetime

from sentidos.som import FREQUENCIA, doppler

print (FREQUENCIA)
doppler()


exit ()

#r = subprocess.run (['free','-h'], stdout=subprocess.PIPE)
#print (r.stdout.decode('utf-8'))

r = run (['apt-get','install','-y','sl'], stdout=PIPE, stderr=PIPE)
if  r.returncode !=0:
 print ('Deu ruim...')

letras = ['A','B','C','D']

print(random.randint(100,999))

time.sleep(2)

print(random.choice(letras))
print (datetime.now())

hoje =datetime.now()
print (hoje.strftime('%d/%m/%Y'))


