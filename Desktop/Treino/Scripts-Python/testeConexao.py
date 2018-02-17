import socket
import urllib3

confiaveis = ['www.google.com','www.yahoo.com','www.bb.com.br']
msg  = 'GET http://google.com/ HTTP/1.1'

def check_host():
	global confiaveis
	host = confiaveis[0]

	http = urllib3.PoolManager()
	req = http.request('GET',host)

	if req.status == 200:
		print('Voce possui acesso a internet')
	else :
		print('Voce nao possui  acesso a internet ')


check_host()