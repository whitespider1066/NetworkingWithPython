# This is a simple client program from lesson 5 of the Futurelearn
# Networking with Python Course.
# Please note not my code! But these are my comments!!!

# those import libraries that are needed
import socket

def get_text(receiving_socket):
	buffer = ""
	
	socket_open = True
	while socket_open:
		# read any data from the socket
		data = receiving_socket.recv(1024)
		
		# if no data is returned the socket must be closed
		if not data:
			socket_open = False
			
		# add the data to the buffer
		buffer = buffer + data.decode()
		
		# is there a terminator in the buffer?
		terminator_pos = buffer.find("\n")
		# if the value is greater than -1, a \n must exist
		while terminator_pos > -1:
			# get the message from the buffer
			message = buffer[:terminator_pos]
			#remove the message from the buffer
			buffer = buffer[terminator_pos + 1:]
			# yield the message
			yield message
			# is there another terminator in the buffer
			terminator_pos = buffer.find("\n")

# create a socket
# AF_INET specifies use IPv4
# SOCK_STREAM denotes TCP, so a TCP/IP socket is created
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server socket
# 127.0.0.1 is the IP address reserved for the internal address of the 
# computer, also known as localhost
client_socket.connect(("127.0.0.1",8081))

print("connected")

# receive data from the socket using the new function
message = next(get_text(client_socket))


print(message)

# close our client socket
client_socket.close()

# Testing
# Make sure that the lesson 4 server is running before running this 
# client script
