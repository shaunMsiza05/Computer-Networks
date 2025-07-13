import socket

def startClientSocket(ipAddress ='localhost'):
    #for now, the function will only take an ip address as a parameter since port numbers are generated randomly for client sockets
    clientSocket = socket.socket()
    clientSocket.bind(ipAddress)
    return clientSocket

