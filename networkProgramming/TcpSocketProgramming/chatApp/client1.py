import socket

clientSocket = socket.socket()

clientSocket.bind(('localhost', 1025))
serverPort = 1024

clientSocket.connect(('localhost', serverPort))


print(clientSocket.recv(1024).decode())



def composeMessage(username, message):
    payload = {"username": username,
               "message": message}
    clientSocket.send(bytes(str(payload), 'utf-8'))
    print(clientSocket.recv(1024).decode())

composeMessage("Bob", "Hi Alice")