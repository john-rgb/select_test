import socket
import os

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)
print('waiting')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while 1:
    conn, addr = sk.accept()
    while 1:
        date = conn.recv(1024)
        cmd, filename, filesize = str(date, 'utf8').split('|')

        path = os.path.join(BASE_DIR, 'yuan', filename)
        print(path)
        filesize = int(filesize)

        f = open(path, 'ab')
        has_sent = 0

        while has_sent != filesize:
            data = conn.recv(1024)
            f.write(data)
            has_sent += len(data)

sk.close()