import socket

#the server maps the username of clients to ports, since I'm stuck to localhost
#there should also be a user registeration method
# the message format should specify the username of the receipient.

#these are the processes of the server
# it should maintain info about the user being active or not.
# When the user connects to the server, the server should change the active status to true, check if any messages are destinated to the user, if so, the message should be sent immediately
# so what data structure should we use to hold messages
# the user will receive the username and resolve it to its ip address
# I'm overthinking this, the aim of the app is for the server to relay the message. I will handle the other parts afterward

clientsData = [
    {"username": "Alice", "port": 1025, "Active": False, "messages": []},
    {"username": "Bob", "port": 1026, "Active": False, "messages": []}
]


# the queued messages will also be stored as objects containing username and the payload

clientUserNames = [["Alice", 1025, False, ["Hi. From Bob", "Hi from steve"]], ["Bob", 1026, False, []]]


socketObjectsOfActiveUsers = []
portsOfActiveUsers = []

def activateUser(userAddress):
    for i in clientUserNames:
        if i[1] == userAddress:
            i[2] = True

def checkAndSendMesages(userAddress, connection):
    clientMessages = ""
    for i in clientUserNames:
        if i[1] == userAddress:
            if len(i[3]) == 0:
                connection.send(bytes("No messages available", 'utf-8'))
            else:
                for j in i[3]:
                    clientMessages = clientMessages + j + "\n"
                    connection.send(bytes(clientMessages, 'utf-8'))
                    i[3] = []
    
                    
                    
#the function assumes that the destination exists, you'll add the fancy features later
# for now write ugly code, you'll add elegant later

def resolveUserName(username):
    for i in clientUserNames:
        if i[0] == username:
           print(i[1])

def sendMessage(destinationAddress, message, sendingUserSocket):
    for i in range(0, len(portsOfActiveUsers)):
        if portsOfActiveUsers[i] == destinationAddress:
            socketObjectsOfActiveUsers[i].send(bytes(message))
            print("The user is active")
    sendingUserSocket.send(bytes("The user is inactive", "utf-8"))
        
serverSocket = socket.socket()

serverSocket.bind(('localhost', 1024))

serverSocket.listen(2)
while True:
    connection, addr = serverSocket.accept()
    #print(connection, addr)
    #when the user connects, we activate their status, for now, let's assume no new users
    # the message is an object that contains a payload and a username
   # connecting to the server will send the client socket, access it's port first
    client_ip, client_port = addr
    #portsOfActiveUsers.append(client_port)
    #socketObjectsOfActiveUsers.append(connection)

    #activateUser(client_port)

    #checkAndSendMesages(client_port, connection)

    

    #now test this if statement
    #the if statement doesn't work
    clientMessage = connection.recv(1024).decode()
    clientMessageObject = {}
    if clientMessage == '':
        print("There's no message")
    else:
        print("There's a message")
        #clientMessageObject = eval(connection.recv(1024).decode())
        #sendMessage(resolveUserName(clientMessage["username"]), str(clientMessage), connection)
    
    #now we handle the stages of sending the messages
    # if the user is inactive, queue the message
    
    
    

