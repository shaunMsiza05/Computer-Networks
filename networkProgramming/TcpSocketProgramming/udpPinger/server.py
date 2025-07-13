import socket

serverSocket = socket.socket()

serverSocket.bind(('localhost', 1024))

serverSocket.listen(100)

