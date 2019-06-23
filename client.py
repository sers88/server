import socket
import argparse
import time
import struct


class Client():

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        '''послать на серверную часть сигнал отключения'''
        self.key = key
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # b = bytes('get %s\n' % (self.key), 'utf-8')
        adress_serv = (self.host, self.port)
        sock.sendto(b'shutdown', adress_serv)
        data, server = sock.recvfrom(4096)
        print("server ", server, "data ", data)
        sock.close()

    def wake_up(self, macadress):
        '''включить удаленный пк по маку'''
        self.macadress = macadress
        wake = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        wake.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        adress_serv = (self.host, self.port)
        wake.connect(adress_serv)
        wake.send(self.macadress)
        wake.close()


def create_magic_packet(macaddress):
    '''функция создания пакета включения по сети'''
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

parser = argparse.ArgumentParser(description='Process something intrest')
parser.add_argument('--key', help='input key')
agra = parser.parse_args()

if agra.key == 'get':
    adress = '192.168.2.64'
    port = 11111
    ksantd_pc = Client(adress, port)
    ksantd_pc.get('shutdown')
elif agra.key == 'wake':
    macadress = '70.71.bc.ad.08.1f'
    adress = '255.255.255.255'
    port = 9
    ksantd_pc = Client(adress, port)
    ksantd_pc.wake_up(create_magic_packet(macadress))
else:
    print('unknow attribute')
