#/usr/bin/env python
#-*- coding:utf-8 -*-
import socket, select, string, sys
import time

# main function
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((host, port))
    except:
        print('Unable to connect')
        sys.exit()
    print('Connected to remote host. Start sending messages')
    rlist = [s, ]
    while 1:
        read_list, write_list, error_list = select.select(rlist, [], [])
        for sock in read_list:
            if sock == s:
                sock.send('hello'.encode('utf-8'))
                data = sock.recv(2048)
                if not data:
                    continue
                else:
                    sys.stdout.write(data)
            else:
                msg = input("我说： ")
                s.sendall(msg)