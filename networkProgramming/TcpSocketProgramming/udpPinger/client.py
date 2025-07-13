import socket

clientSocket = socket.socket()

clientSocket.bind()

# calculate the round trip time
# you'll add the other ping messages afterwards, in fact, write traceroute afterwards

def sendPingMessage(destinationPort):
    clientSocket.connect('localhost')