# This is a simple client program from lesson 5 of the Futurelearn
# Networking with Python Course.
# Please note not my code! But these are my comments!!!

# those import libraries that are needed
import socket

# create a socket
# AF_INET specifies use IPv4
# SOCK_STREAM denotes TCP, so a TCP/IP socket is created
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server socket
# 127.0.0.1 is the IP address reserved for the internal address of the 
# computer, also known as localhost
client_socket.connect(("127.0.0.1",8081))

print("connected")

# receive data from the socket upto a maximum of 1024 characters
data = client_socket.recv(1024)

# decode the received data
message = data.decode()

print(message)

# send a message back to the server
message = "Thanks for the fish!"
data = message.encode()
client_socket.send(data)

# close our client socket
client_socket.close()

# Testing
# Make sure that the lesson 4 server is running before running this 
# client script
