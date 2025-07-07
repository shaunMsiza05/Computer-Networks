# for now, make the requests through this client socket. But when  you start refining the code, add a basic html file for a browser UI

import socket
import json

clientSocket = socket.socket()

clientSocket.bind(('localhost', 1025))

def searchForResourceRecord(resourceRecords, type, domainName):

    if type == 'A':
        index = 0
        for i in resourceRecords['A']:
            if i[0] == domainName:
                return i[1]
            
def dnsResolver(domainName, type):

    resourceRecords = {
        "A": [
            ("web.amazon.com", "localhost", "A", 10),
            ("mail.amazon.com", "localhost", "A", 10),
            ("web.facebook.com", "localhost", "A", 10),
            ("mail.facebook.com", "localhost", "A", 10)
        ],
        "MX": [
             ("facebook.com", "mail.facebook.com", "MX", 10),
             ("amazon.com", "mail.amazon.com", "MX", 10)
        ],
        "CNAME": [
            ("facebook.com", "web.facebook.com", "CNAME", 10),
            ("amazon.com", "web.amazon.com", "CNAME", 10)
        ]
    }

    return searchForResourceRecord(resourceRecords, type, domainName)



def makeRequest(url):
    urlParts = url.split("/")
    objectRequested = ""
    #objectRequested = [urlParts[i] for i in range(1, len(urlParts) - 1)]
    for i in range(1, len(urlParts)):
        objectRequested += "/" + urlParts[i]
    getRequestObject = {
        "get": f"GET {objectRequested} HTTP/1.1",
        "Host": urlParts[0],
        "user-agent": "Chrome 4.6",
        "connection": "close"
    }
    clientSocket.connect((dnsResolver(getRequestObject["Host"], "A"), 1024))
    clientSocket.send(bytes(json.dumps(getRequestObject), 'utf-8'))

makeRequest("web.amazon.com/somedir/page.html")
#print(dnsResolver("web.amazon.com", "A"))