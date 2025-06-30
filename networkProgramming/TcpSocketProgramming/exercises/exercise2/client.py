
import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

filename = "fileToSend.txt"  # replace with your file name
client_socket.sendall(filename.encode())

with open(filename, "rb") as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)

print(f"File {filename} sent successfully")
client_socket.close()