'''
Created on 8 mars 2021

@author: tdiard
'''
import socket
import threading
import json

class ThreadForClient(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn= conn

    def run(self):
        data = self.conn.recv(1024)
        data = json.loads(data.decode("utf-8"))
        print(data)

host, port = ('',5566)

ServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ServerSocket.bind((host,port))
print("Server Started")
while True:
    ServerSocket.listen(5)
    conn,address = ServerSocket.accept()
    print("Listening ...")
    Thread = ThreadForClient(conn)
    Thread.start()

conn.close()
ServerSocket.close()