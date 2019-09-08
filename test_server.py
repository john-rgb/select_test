# coding: utf-8
import select
import socket
from queue import Queue
from time import sleep


# Create a TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# Bind the socket to the port
server_address = ('localhost', 8090)
print('starting up on %s port %s' % server_address)
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Sockets from which we expect to read
inputs = [server]

# Sockets to which we expect to write
# 处理要发送的消息
outputs = [server]

# Outgoing message queues (socket: Queue)
message_queues = {}

while True:
    # Wait for at least one of the sockets to be ready for processing
    print('waiting for the next event')
    # 开始select 监听, 对input_list 中的服务器端server 进行监听
    # 一旦调用socket的send, recv函数，将会再次调用此模块
    # print(server,'++++++++++++')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # print(readable,writable)
    for read in  readable:
        if read is server:
            conn,addr=read.accept()
            print(read,'---------',conn)
            outputs.append(conn)
            # print('--------------')
        else:
            print('++++++++++')
    for write in writable:
        print('aaaaaaaaaaaaaaaa',write)
        outputs.remove(conn)


