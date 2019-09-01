import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8004))

content = str(obj.recv(1024), encoding='utf-8')
print(content)

obj.close()

# 客户端c2.py
