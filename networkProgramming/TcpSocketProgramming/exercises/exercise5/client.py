import socket

clientSocket = socket.socket()

clientSocket.connect(('localhost', 1024))

randomInput = "Testing server socket"
clientSocket.send(bytes(randomInput, 'utf-8'))

clientSocket.close()