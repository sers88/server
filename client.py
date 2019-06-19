import socket
import os
import time

class Client():

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        self.key = key
        sock = socket.create_connection((self.host, self.port))
        b = bytes('get %s\n' % (self.key), 'utf-8')
        sock.sendall(b)
        sock.close()
