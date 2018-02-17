import socket
#Servidor somente faz um eco da msg enviada pelo cliente
Host = ''

Port = 50007

obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

obj.bind((Host,Port))

obj.listen(3)

while True:
	conexao, endereco = obj.accept()
	print('Server  conectado por', endereco)
	while True:	
		data = conexao.recv(1024)

		if not data: 
			break

		conexao.send(data)

	obj.close()