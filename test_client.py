# coding: utf-8
import socket


messages = ['This is the message ', 'It will be sent ', 'in parts ', ]

server_address = ('localhost', 8090)

# Create aTCP/IP socket

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect thesocket to the port where the server is listening

print ('connecting to %s port %s' % server_address)
# 连接到服务器
socks.connect(server_address)
while True:
    recv_data=socks.recv(1024)
    print(recv_data.decode())