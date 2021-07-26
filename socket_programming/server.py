import socket

# By default, socket uses IPv4 and TCP protocol
server = socket.socket()

server.bind(('127.0.0.1', 9999))

# Mention how many connections to accept to the listen() method
server.listen()

print("Waiting for connections")

while True:
    client, address = server.accept()

    name = client.recv(1024).decode()
    print(f"Connected with {address} {name}")

    client.send(b"Welcome to server")

    client.close()

# Note:
# The server socket doesn't send any data and server socket doesn't receives any data.
# Server socket only produces the client sockets.
# Each client socket is created in response to some other client socket doing a connect() to the
# host and port we're bound to.
# The two clients are free to chat it up.
