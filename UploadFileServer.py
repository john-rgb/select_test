#-*- coding:utf-8 -*-
import getopt
import sys
import socket
import os
import select
import queue

def Usage():
    print('[-]UploadFileServer.py -h/--help ####To see how to use this program.')
    print('[-]UploadFileServer.py -i ip -p port ####Tet ip and port to open server program. eg:UploadFileServer.py -i 192.168.1.1 -p 8080')
def GetFileName():
    pass

def main():

    opts,args=getopt.getopt(sys.argv[1:],'hi:p:',["help",])
    print(len(opts))
    for para_1,para_2 in opts:
        if para_1 in ['-h',"--help"]:
            print(Usage())
            sys.exit()
        if para_1 in ["-i"]:
            ip=para_2
        if para_1 in ["-p"]:
            port=para_2
    server=socket.socket()
    server.bind((ip,int(port)))
    server.listen(5)
    inputs=[server,]
    outputs=[]
    message_queue={}
    while True:
        readable, writeable, exceptional = select.select(inputs, outputs, inputs)
        for read in readable:
            if read is server:#first case
                conn,addr=read.accept()
                inputs.append(conn)
                message_queue[conn]=queue.Queue()
                print('------------')
                # read.sendall("connect success".encode('utf-8'))
            else:#second case
                # read.sendall("connect success".encode('utf-8'))
                data = read.recv(1024)
                if data:
                     # read.send(data)
                    message_queue[read].put(data)
                    if read not in outputs:
                        outputs.append(read)
                else:
                    if read in outputs:
                        outputs.remove(read)
                    inputs.remove(read)
                    read.close()
                    del message_queue[read]
        for write in writeable:
            try:
                next_msg=message_queue[read].get_nowait()
            except queue.Empty as e:
                outputs.remove(write)
            else:
                write.send(next_msg)
        for excep in exceptional:
            inputs.remove(read)
            for write in outputs:
                outputs.remove(write)
            read.close()
            del message_queue[read]


if __name__=="__main__":
    main()
