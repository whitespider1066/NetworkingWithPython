# Week 1 Project: A Chat Application
# by Darren Christie
# Please not this is my code but based on the project outline for the 
# lesson.

# those import libraries that are needed
import socket

print ("Networking with Python Week 1 Project, A Chat Application\n")

option = input("Enter 1. to run as server, Enter 2. to run as client. ")


if option == "1":
	print ("Entering server mode\n")
	openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	openSocket.bind(("0.0.0.0",8081))
	
	openSocket.listen()
	print("waiting for connection")
    
	connectionSocket, address = openSocket.accept()
	print("client connected")
else:
	print ("Entering client mode\n")
	connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverAddress = input("Enter the IP Address of server to connect to: ")
	connectionSocket.connect((serverAddress,8081))
	connectionSocket.send(bytes("Hello",'utf-8'))
	print ("Connected")
	
running = True
while running:
	message = connectionSocket.recv(1024)
	print(message.decode())
	newMessage = input("Enter a message: ")
	if newMessage == "E":
		running = False
	else:
		connectionSocket.send(newMessage.encode())

print ("Closing sockets\n")

connectionSocket.close()
if option == "1":
	openSocket.close()
