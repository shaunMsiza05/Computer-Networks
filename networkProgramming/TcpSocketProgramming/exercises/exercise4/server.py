import socket 

ConnectedClients = []

port = 1028
host = 'localhost'

serverSocket = socket.socket()
serverSocket.bind((host, port))

serverSocket.listen(100)
print(f"server is listening at port {port}")

def AddClient(clientSocketObject):
    ConnectedClients.append(clientSocketObject)

def broadcastMessage():
    if len(ConnectedClients) == 0:
        print("There are not client connections")
    else:
        for i in ConnectedClients:
            i.send(bytes(connection.recv(1024), 'utf-8'))

while True:
    connection, addr = serverSocket.accept()
    print(f"{addr} has connected successfully")
    AddClient(connection)
    broadcastMessage()
    connection.close()


