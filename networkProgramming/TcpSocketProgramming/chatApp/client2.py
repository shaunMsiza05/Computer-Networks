import socket

clientSocket = socket.socket()

clientSocket.bind(('localhost', 1026))
serverPort = 1024

clientSocket.connect(('localhost', serverPort))


print(clientSocket.recv(1024).decode())
