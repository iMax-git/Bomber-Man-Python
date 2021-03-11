'''
Created on 8 mars 2021

@author: tdiard
'''
import socket
import threading
from _thread import *
import json

class ThreadForClient(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn= conn

    def run(self):
        data = self.conn.recv(1024)
        data = json.loads(data.decode("utf-8"))

pos = [(0,0),(100,100)]

def make_pos(tup):
    return str(tup[0])+","+str(tup[1])


def read_pos(str):
    str = str.split(",")
    print(str[0],str[1])
    return (int(str[0]),int(str[1]))

def Thread_Client(conn,player):
    print(player)
    conn.send(str.encode(make_pos(pos[player])))
    
    reply =''
    while True:
        try:
            data = read_pos(conn.recv(1024).decode())
            pos[player] = data
            if not data:
                print("Disconnected !")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: "+reply)
                print("Sending: "+reply)
            conn.sendall(str.encode(reply))
        except:
            break


host, port = ('192.168.1.26',5566)

ServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ServerSocket.bind((host,port))
print("Server Started")

currentPlayer = 0
while True:
    ServerSocket.listen(5)
    conn,address = ServerSocket.accept()
    start_new_thread(Thread_Client,(conn, currentPlayer))
    # currentPlayer += 1

conn.close()
ServerSocket.close()