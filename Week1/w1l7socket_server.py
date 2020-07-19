# This is a simple server program from lesson 4 of the Futurelearn
# Networking with Python Course.
# Please note not my code! But these are my comments!!!

# those import libraries that are needed
import socket

# function to append a new line character (\n) to the end of message
# then send the encoded message on the supplied socket
def send_text(sending_socket, text):
	text = text + "\n"
	data = text.encode() # defaults to utf-8 for encoding
	sending_socket.send(data)
	


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

message = "Hello, thanks for connecting"

# send our message to the client that we connected to
send_text(connection_socket,message)

# close our connection and server sockets
connection_socket.close()
server_socket.close()

# The IP address 127.0.0.1 is an internal address that only programs 
# on this computer can use. It refers to which ever machine running on.
