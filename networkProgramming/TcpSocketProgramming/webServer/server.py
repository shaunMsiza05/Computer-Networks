import socket
import json

serverSocket = socket.socket()

serverSocket.bind(('localhost', 1024))

serverSocket.listen(100)

def checkDirectory(host):
    return ''

def findObject(relativePath)
while True:
    connection, addr = serverSocket.accept()
    print(f"{connection} connected successfully")
    httpRequest = eval(connection.recv(1024).decode())
    hostName = httpRequest["Host"]
    checkDirectory(hostName)
    filePath = httpRequest["get"]
    print(filePath[4:])
    findObject(filePath[4:])
# I didn't plan this web server properly, but this is what is should do. 
#each and every website that runs on it has a corresponding folder idenfied by the host and the folder contains the objects and stuff
# so I must extract the host part of the request and check if folder exists, if not, the website isn't hosted.
# step 2 is to check for the required object
