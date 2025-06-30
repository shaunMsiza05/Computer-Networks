import socket

c = socket.socket()

#pass the ip address of the server and the port number when connecting to the server

c.connect(('localhost', 1050))

name = input("  Enter your name")
c.send(bytes(name, 'utf-8'))
# we print whatever we receive from the server process
#without add decode, the string will be printed with a b

print(c.recv(1024).decode())
