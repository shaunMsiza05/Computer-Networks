import socket

client7Socket = socket.socket()

client7Socket.connect(('localhost', 1028))

#Let's assume this client is Mr Kane

randomMessage = """ From: Mr Kane
One of my favorite coding challenges is solving problems on platforms like LeetCode. It's a great way to practice and learn new concepts. And I'd love to hear more about yor project and how you're approaching database optimisation.
To: Mr Smith """

client7Socket.send(bytes(randomMessage, 'utf-8'))
client7Socket.close()