import socket

serverSocket = socket.socket()

serverSocket.bind(('localhost', 1026))

serverSocket.listen(100)
print('server is listening at port 1026')

while True:
    connection, addr = serverSocket.accept()
    print(f"{connection} {addr} connected succefully")
    connection.send(bytes(connection.recv(1024).decode().upper(), 'utf-8'))
    connection.close()

