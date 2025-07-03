import socket 

clientSocket = socket.socket()
socketPort = 1030
clientSocket.bind(('localhost', socketPort))

clientSocket.listen(100)
print(f"sever socket listeninf at port {socketPort}")
while True:
    connenction, addr = clientSocket.accept()
    print(f"{connenction} connected successfully")
    print(connenction.recv(1024).decode())

