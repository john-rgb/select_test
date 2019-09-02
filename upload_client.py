import socket
import os

sk = socket.socket()
address = ('127.0.0.1', 8004)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 上层文件路径。

while True:
    inp = input('>>>')  # post|filename
    print(inp)

    cmd, path = inp.split('|')

    path = os.path.join(BASE_DIR, path)  # 拼接完整目录

    filename = os.path.basename(path)

    file_size = os.stat(path).st_size  # 获取文件大小

    file_info = 'post|%s|%s' % (filename, file_size)  # 打包

    sk.sendall(bytes(file_info, 'utf8'))  # 编码

    f = open(path, 'rb')
    # file_size=100
    has_sent = 0
    while has_sent != file_size:
        data = input('>>>###')
        sk.sendall(data)
        has_sent += len(data)

    f.close()
    print("上传成功")
sk.close()