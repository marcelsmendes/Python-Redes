import socket

confiaveis = ['www.google.com','www.yahoo.com']

def check_host(confiaveis):
	for host in confiaveis:
		a = socket.socket(spcket.AF_INET,socket.SOCK_STREAM)
		a.settimeout(.55)

		try:
			b = a.connect_ex((host,80))

			if b==0:
				print('Conectado')
				return TRUE
		except :
			pass
	a.close()
	return FALSE