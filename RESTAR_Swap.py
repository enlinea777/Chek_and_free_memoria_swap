import os
import re
f = os.popen('grep Swap /proc/meminfo')
now = f.read()
d=now.split("\n")
print d[1]
dd= d[1].lower()
Memoria_Total = int(re.sub(r'([a-z:\s])', r'', dd))

print d[2]
dd= d[2].lower()
Memoria_libre = int(re.sub(r'([a-z:\s])', r'', dd))
#print 'Memoria_libre ',Memoria_libre

Limite= Memoria_Total - 1024
#print 'Limite ',Limite
mensaje=now + '\nswapoff -a && swapon -a'
if Memoria_libre < 1024:
	print 'no queda memoria'
	f = os.popen('bash VerUsoSwap | sort -n -k 5 ') #usar solo con el codigo para reportar el programa que colapsa el Swap
	now = f.read()
	#print Limite
	os.system('echo "'+now+'\n'+mensaje+'" | mail -s Asunto Correo@electronico.com')
	os.system(" swapoff -a && swapon -a")
	print 'Listo, Liberada'
else:
	print 'Memoria swap Libre'
