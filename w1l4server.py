# those import libraries that are needed
import socket

# create a socket
# AF_INET specifies use IPv4
# SOCK_STREAM denotes TCP, so a TCP/IP socket is created
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
# binds the socket to an address and port
# "0.0.0.0" will bind the socket to all network IP addresse available 
# on the computer this python program is being run.

# 8081 determines the TCP port the socket should use. 8081 is typically 
# used for testing.
server_socket.bind(("0.0.0.0",8081))

# listen
# listen for a connection to be made
server_socket.listen()
print("waiting for connection")

# accept
# wait for a connection and accept it
connection_socket, address = server_socket.accept()
print("client connected")

# Testing this server
# With this code running.
# Use a web browser and enter the following in the URL bar:
# 127.0.0.1:8081

# you should see the two print statements 

# The IP address 127.0.0.1 is an internal address that only programs 
# on this computer can use. It refers to which ever machine running on.
