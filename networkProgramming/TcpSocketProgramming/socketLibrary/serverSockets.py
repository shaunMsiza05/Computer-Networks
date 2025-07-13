import socket

def startServerSocket(ipAddress, portNumber):
    serverSocket = socket.socket()
    serverSocket.bind(ipAddress, portNumber)
    return serverSocket