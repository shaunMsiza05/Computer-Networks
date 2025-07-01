import socket

client6Socket = socket.socket()

client6Socket.connect(('localhost', 1028))

#Let's assume this client is Mr Biden

randomMessage = """ From: Mr Biden
For sorting large datasets, I'd recommend looking into merge sort or quicksort. Both are efficient algorithms with good average-case perfomance. And speaking of efficiency, have you ever used a debugger to optimise your code.
To: Mr Kane""""

client7Socket.send(bytes(randomMessage, 'utf-8'))
client7Socket.close()