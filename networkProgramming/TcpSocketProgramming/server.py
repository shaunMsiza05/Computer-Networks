import socket

#creating a socket
# parameters of the socket function. The first one specifies the ip address type (IPV4 OR IPNG). The second parameter specifies either tcp or udp
#by not specifying the arguments, tcp and ipv4 will be selected by default

s = socket.socket()
print('Socket created')
# remeber from the textbook that if you don't bind a port number, it will be created by default. Avoid well-known port numbers (0 - 1023)

s.bind(('localhost', 1050))

#then you have to start listening to client requests. And you can also specify the number of clinnts that can be connnected.

s.listen(3)
print('waiting for connections')
# the fourth connection won't be accepted

#the while loop ensures that we are accepting requests continuously
while True:
    #this will return the client socket and the address
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", addr, name)
    #this should be sent in a byte format
    c.send(bytes('Welcome to Area 51', 'utf-8'))
    c.close()


