from socket import *


def main():
	serverPort = 5000
	serverHost = "localhost"

	client = socket(AF_INET,SOCK_DGRAM)

	msg = input('--')

	while msg != '0':
		client.sendto(msg.encode(),(serverHost,serverPort))
		data, endereco = client.recvfrom(1024)
		print('Eco',data.decode())
		msg = input('--')

	client.close()

main()