import pickle
import socket
from PIL import Image

# This code uses the Python Imaging Library PIL to open an image and 
# get the image’s dimensions (width and height). 
image = Image.open("image.bmp")

width, height = image.size
print(width, height)

# create a UDP client socket
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Now use the image dimensions (width and height) to loop through 
# each pixel and get the pixel’s colour.
for y in range(height):
    for x in range(width):
        pos = (x, y)
        rgba = image.getpixel(pos)
        # print(pos, rgba)
        
        # Construct a message for each pixel, containing the pos 
        # and rgba values
        message = (pos, rgba)
        
        # convert the message into bytes
        data = pickle.dumps(message)
        
        # Send the pixel data using the udp_client socket.
        udp_client.sendto(data, ("127.0.0.1", 20001))
