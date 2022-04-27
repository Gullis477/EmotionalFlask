from doctest import IGNORE_EXCEPTION_DETAIL
import socket
import time

# Host machine IP
HOST = '127.0.0.1'
# Gazepoint Port
PORT = 4242
ADDRESS = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDRESS)
s.send(str.encode('<SET ID="CALIBRATE_SHOW" STATE="1" />\r\n'))

   