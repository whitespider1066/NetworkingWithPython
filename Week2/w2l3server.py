# UDP Server
import socket

# create a socket that uses UDP (SOCK_DGRAM)
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set up port to accept data from all network addresses
# port 20001 is used for testing UDP
udp_server.bind(("0.0.0.0", 20001))

data, client_address = udp_server.recvfrom(1024)
udp_server.sendto(data, client_address)
