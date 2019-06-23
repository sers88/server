import socket
import os
import time
import struct

class Client():

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        self.key = key
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # b = bytes('get %s\n' % (self.key), 'utf-8')
        adress_serv = (self.host, self.port)
        sock.sendto(b'ffff', adress_serv)
        data, server = sock.recvfrom(4096)
        print("server ", server, "data ", data)
        sock.close()

    def wake_up(self, macadress):
        self.macadress = macadress
        wake = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        wake.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        adress_serv = (self.host, self.port)
        wake.connect(adress_serv)
        wake.send(self.macadress)
        wake.close()

    '''def str_to_mac(self):
        hex_macs = self.mac*16
        full_wake = self.byting+hex_macs
        return full_wake'''

def create_magic_packet(macaddress):

    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')

    data = b'FFFFFFFFFFFF' + (macaddress * 16).encode()
    send_data = b''

    for i in range(0, len(data), 2):
        send_data += struct.pack(b'B', int(data[i: i + 2], 16))
    return send_data

macadress = '70.71.bc.ad.08.1f'
adress = '255.255.255.255'
port = 9
ksantd_pc = Client(adress, port)
# ksantd_pc.get('lohi')
ksantd_pc.wake_up(create_magic_packet(macadress))
