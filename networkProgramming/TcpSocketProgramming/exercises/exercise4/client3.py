import socket

client3Socket = socket.sockett()

client3Socket.connect('localhost', '1028')

# let's call this client Mrs Brown

randomMessage = """From: Mrs Brown
Indexing is a great point. I've also found that caching can be helpful. Speaking of programming languages, I'm a big fan of Python for database work. What about you? And have you worked with any interesting data structures recently?
To: Ms Jane"""
print(client.recv(1024).decode())
client3Socket.close()