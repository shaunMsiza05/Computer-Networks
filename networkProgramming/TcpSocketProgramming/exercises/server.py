import socket

serverSocket = socket.socket()

serverSocket.bind(('localhost', 1024))

serverSocket.listen(1)
print('socket created')
print('waiting for connections')
while True:
    c, addr = serverSocket.accept()
    print("Connected with", addr)
    c.send(bytes(c.recv(1024).decode(), 'utf-8'))
    c.close()