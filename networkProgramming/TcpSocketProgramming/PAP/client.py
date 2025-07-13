import socket

clientSocket = socket.socket()

clientSocket.connect(('localhost', 4000))

def sendAuthentication(username, password):
    clientSocket.send(bytes(str({
        "username": username,
        "password": password
    }), 'utf-8'))


sendAuthentication("SiteA", "1234")
print(clientSocket.recv(1024).decode())