import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server is listening on {host}: {port}")

connection, client_address = server_socket.accept()
print(f"Connected to {client_address}")

filename = connection.recv(1024).decode()
print(f"Receiving file: {filename}")

with open(f"received_{filename}", "wb") as f:
    while True:
        data = connection.recv(1024)
        if not data:
            break
        f.write(data)

print(f"File {filename} received successfully")
connection.close()