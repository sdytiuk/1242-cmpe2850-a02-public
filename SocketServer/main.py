# echo-server.py
import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the hostname
host = socket.gethostname()
print(host)
# choose a port number
port = 1666

# bind the socket object to the host and port, this could throw if the network is unavailable or the port is already bound.
server_socket.bind((host, port))

# listen for incoming connections, let 5 connections queue up
server_socket.listen(5)

# accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connected by {client_address}")

# receive and send back the data
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    client_socket.sendall(data)

# close the connection
client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()