import socket


Host = 'localhost'
Port = 50007

msg = input('Digite a mensagem: ')

obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
obj.connect((Host,Port))
#msg.encode()

#for linha in msg:
obj.send(msg.encode())

data = obj.recv(1024)

print('Cliente recebeu: ', data.decode())
