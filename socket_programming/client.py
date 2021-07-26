import socket

# By default, socket uses IPv4 and TCP protocol
client = socket.socket()

# Connecting to the server using socket. Socket is simply an combination of an IP and port.
client.connect(('127.0.0.1', 9999))

name = input("Enter the name: ")
client.send(bytes(name, 'utf-8'))

print(client.recv(1024).decode())
