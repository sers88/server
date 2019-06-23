import socket
import os
import time

class Server():

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def lisning(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((self.host, self.port))
        print("At start server BY")
        data, client = server.recvfrom(4096)
        print('client ', client, 'data ', data)
        server.sendto(b'ololol ', client)
        server.close()

'''adress = "localhost"
port = 11111
ksantd_serv = Server(adress, port)
ksantd_serv.lisning()'''
