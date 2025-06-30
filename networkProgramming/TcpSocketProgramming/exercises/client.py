import socket

clientSocket = socket.socket()

clientSocket.connect(('localhost', 1024))
messageToTheServer = input("Add a message to send to the server ")
clientSocket.send(bytes(messageToTheServer,'utf-8'))
print(clientSocket.recv(1024).decode())

