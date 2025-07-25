import socket
import random
# simulate lcp negotiation

# because I am working on one terminal, I will distinguish devices with ports
# three main parameters should be compared: magic number, mru

# the logic on both ends should be the same, since peers are always listening
# fuck surface level, you should also code the ppp encapsulation to distinguish between acknoweldgement and request
LCPParameters = {
    "MRU": 2000,
    "Auth_Type": "PAP",
    "Magic_Num": random.randint(0, 100)
}

peerAddress = ('localhost', 1024)
def configureRequest(peerAddress):
    clientSocket = socket.socket()
    clientSocket.connect(peerAddress)
    clientSocket.send(bytes(str(LCPParameters), 'utf-8'))
    #test socket

# this method should compare the received request with its lcp parameters, specificallly the MRU since that's the only negotiable parameter
# identify conflicting magic numbers

def configureACK(PeerLCPParameters):
    if PeerLCPParameters["Magic_Num"] == LCPParameters["Magic_Num"]:
        #identify the link loop or write the control message
    #else:
        if LCPParameters["MRU"] == LCPParameters["MRU"]:
            configureACK()
            configureRequest()


configureRequest(peerAddress)

#this process is a bit more complex than I expected, I think it's better if I design the entire system first, for now, I'll just do a raw simulation, add elegance tommorow
# but one main LCP negotiation function will be used for flow control
