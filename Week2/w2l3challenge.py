# UDP Server
import socket

# create a socket that uses UDP (SOCK_DGRAM)
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = input("Enter server address: ")

message = "Hello dolly"

udp_server.sendto(message.encode(), (server_address,20001))
data, client_address = udp_server.recvfrom(1024)
print(data)
