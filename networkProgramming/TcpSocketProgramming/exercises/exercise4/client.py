import socket 

clientSocket = socket.socket()

clientSocket.connect(('localhost', 1028))

# send a random message
# The client assumes that the server will broadcast the message, therefore, let's send greetings to Mr Harvey
# let's assume this client is Mr Smith
randomMessage = "Hello Mr Harvey"
clientSocket.send(bytes(randomMessage, "utf-8"))
print(clientSocket.recv(1024).decode())


