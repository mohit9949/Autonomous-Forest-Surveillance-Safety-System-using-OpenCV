"""#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
port = 12333             # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('1 0 1 0 hu11 tr11')
   c.send('1 1 1 0 hu11 tr11')
   c.close()                # Close the connection"""
import socket

TCP_IP = '192.168.43.253'
TCP_PORT = 8001
BUFFER_SIZE = 1000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send('QUIT')
s.close()
