import socket

clientSocket = socket.socket()

clientSocket.connect(('localhost', 1026))

clientSocket.send(bytes('lowerCaseWord', 'utf-8'))

upperCaseWordFromServer = clientSocket.recv(1024).decode()

print(upperCaseWordFromServer)

clientSocket.close()
