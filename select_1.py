import socket

HOST = 'localhost'
PORT = 10001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    # data = s.recv(1024)
    # print('Received', data.decode())
    msg = bytes(input(">>:").strip(), encoding="utf-8")
    if msg == 'q'.encode("utf-8"):
        exit("退出！")
    s.sendall(msg)
    data = s.recv(1024)
    print('Received', data.decode())
s.close()