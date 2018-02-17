from socket import *

def main():
	host = ''
	port = 5000

	server = socket(AF_INET,SOCK_DGRAM)
	server.bind((host,port))

	print('servidor iniciado')

	while True:
		data, endereco = server.recvfrom(1024)
		server.settimeout(10)	#tempo limite para resposta 10 segundos
		print('Msg recebida de ',endereco)
		print('Recebida do cliente os seguintes dados\n ',data.decode())

		server.sendto(data,endereco)

	server.close()#conexão persistente


main()