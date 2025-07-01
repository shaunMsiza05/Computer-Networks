import socket

client4Socket = socket.socket()

client4Socket.connect('localhost', 1028)

#Let's assume this client is Ms Jane

randomMessage = """From: Ms Jane 
Ah yes! Big O Notation is crucial for understanding algorithm efficiency. I've beeen studying it recently. And linked lists are indeed useful. I've been working on a project that requires efficiency sorting of large datasets. Do you have suggestions on  algorithms to use?
To Mr Kane"""

client4Socket.send(bytes(randomMessage, 'utf-8'))
client4Socket.close()
