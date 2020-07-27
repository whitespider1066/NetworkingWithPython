import socket
import pickle
from fl_networking_tools import ImageViewer


# a function that will wait for data to be received on the UDP socket.
def get_pixel_data():

    lost_pixels = 0
    last_pixel_updated = (-1, -1)
    while True:
        data, client_address = udp_server.recvfrom(1024)
        
        # The message sent is a tuple of the pixel’s pos and 
        # rgba values. Unpickle the message and split it into its 
        # component parts.
        message = pickle.loads(data)
        pos = message[0]
        rgba = message[1]
        
        if (pos[0] - last_pixel_updated[0] > 1) or (pos[1] - last_pixel_updated[1] > 1):
            lost_pixels += 1
            viewer.text = lost_pixels
        last_pixel_updated = pos
        
        # passed the position and values for a pixel, 
        # will put it onto the screen
        viewer.put_pixel(pos, rgba)

        # Output how many pixels have been lost
        viewer.text = lost_pixels

# create a server
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("0.0.0.0", 20001))

viewer = ImageViewer()

# start the image viewer
viewer.start(get_pixel_data)
