import socket 

clientSocket = socket.socket()

clientSocket.connect(('localhost', 1028))

# send a random message
# The client assumes that the server will broadcast the message, therefore, let's send greetings to Mr Harvey
# since this is a broadcast means of communication, so the sender must identify themselves and the destination
# then the second chat app must be unicast commmunication, if the port is unkown, then it should be broadcast
# let's assume this client is Mr Smith
randomMessage = """ From: Mr Smith
Hey, I'm working on a project that requires optimising database perfomance. Do you have any tips on how to improve query speed.
To: Mr Harvey"""
clientSocket.send(bytes(randomMessage, "utf-8"))
print(clientSocket.recv(1024).decode())
clientSocket.close()

