import socket
import select
import os

server = socket.socket()
server.bind(('0.0.0.0', 8004))
server.listen()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)


inputs = [server,]

while True:
    r_list, w_list, e_list = select.select(inputs,[],inputs,1)
    # print('222222222')
    for sk in r_list:
        print('sssssssssssssss')
        print(sk)
        if sk is server:
            conn, address = server.accept()
            inputs.append(conn)
        # conn表示每一个连接对象


        # print(conn)
        # conn.sendall(bytes('hello', encoding='utf-8'))
        while 1:
            print('++++++++++++')
            data = conn.recv(1024)
            print(data)
            cmd, filename,filesize = str(data, 'utf8').split('|')
            # print(filesize)
            path = os.path.join(BASE_DIR, 'yuan', filename)
            print(path)
            filesize=100
            filesize = int(filesize)
            f = open(path, 'ab')
            has_sent = 0
            while has_sent!=filesize:
                data=conn.recv(1024)
                print('-----------')
                print(data)
                f.write(data)
                has_sent+=len(data)
            print('=============')
            f.close()
        conn.close()

    for sk in e_list:
        inputs.remove(sk)