import select
import socket
import sys
import queue
import os

# create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# Bind the socket to the port
server_address = ('localhost', 10000)
server.bind(server_address)

# Listen for incoming connections
server.listen(1000)

inputs = [server, ]
outputs = []
while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)
    for r in readable:
        if r is server:  # 代表来了一个新连接
            conn, addr = server.accept()
            print("来了一个新连接", conn, addr)
            inputs.append(conn)  # 是因为这个新建立的连接还没发数据过来，现在就接收的话程序就报错，
            # 所以要想实现这个客户端发数据来时server端能知道就需要让select再检测这个conn
        else:
            data = r.recv(1024)
            print("收到的数据：", data.decode())
            r.send(data)
            print("send done....")