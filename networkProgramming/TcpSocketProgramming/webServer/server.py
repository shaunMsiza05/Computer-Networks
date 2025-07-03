import socket

serverSocket = socket.socket()

serverSocket.bind(('localhost', 1024))

serverSocket.listen(100)

while True:
    connection, addr = serverSocket.accept()
    print(f"{connection} connected successfully")
    print(connection.recv(1024).decode())

