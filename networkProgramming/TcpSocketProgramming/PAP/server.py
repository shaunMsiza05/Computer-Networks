import socket


authenticationDataBase = [("SiteA", "1234")]

serverSocket = socket.socket()

serverSocket.bind(('localhost', 4000))


serverSocket.listen(1)

def authenticator(userInfo: tuple[str, str]):

    for i in authenticationDataBase:
        if userInfo == i: 
            return True
    return False
    
while True:
    connection, addr = serverSocket.accept()
    userInfo = eval(connection.recv(1024).decode())
    if authenticator((userInfo["username"], userInfo["password"])):
        connection.send(bytes('Authenticated succesfully', 'utf-8'))
    else:
        connection.send(bytes('Authenticated failed', 'utf-8'))
        connection.close()

    





