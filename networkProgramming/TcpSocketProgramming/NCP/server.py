import socket
import random
import select
# simulate lcp negotiation

# because I am working on one terminal, I will distinguish devices with ports
# three main parameters should be compared: magic number, mru

# the logic on both ends should be the same, since peers are always listening

LCPParameters = {
    "MRU": 2000,
    "Auth_Type": "CHAP",
    "Magic_Num": random.randint(0, 100)
}

peerAddress = ('localhost', 1025)
def configureRequest(peerAddress):
    clientSocket = socket.socket()
    clientSocket.connect(peerAddress)
    clientSocket.send(bytes(LCPParameters, 'utf-8'))

serverSocket = socket.socket()

serverSocket.bind(('localhost', 1024))

serverSocket.listen(1)

print("server is listening")

def configureACK(PeerLCPParameters, peerSocket):
    if PeerLCPParameters["Magic_Num"] == LCPParameters["Magic_Num"]:
        #identify the link loop or write the control message
    #else:
        if LCPParameters["MRU"] == LCPParameters["MRU"]:
            #placeholder for more serious code
            configureRequest(peerAddress)

while True:
    connection, addr = serverSocket.accept()
    print(f"{connection}, has connected")
    ready, _, _ = select.select([connection], [], [], None)

    if connection in ready:
        data = connection.recv(1024)

        
        if data:
        # Safe to proceed
           print(data)
           configureACK(eval(data), connection)