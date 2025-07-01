import socket

client5Socket = socket.socket()

client5Socket.connect('localhost', 1028)

#Let's assume this client is Mr Kane

randomMessage = """ From: Mr Kane
For sorting large datasets, I'd recommend looking into merge sort or quicksort. Both are efficient algorithms with good average-case perfomance. And speaking of efficiency, have you ever used a debugger to optimise your code?
To: Ms Jane"""

client5Socket.send(bytes(randomMessage, 'utf-8'))
client5Socket.close()
