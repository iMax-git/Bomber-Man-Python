'''
Created on 10 mars 2021

@author: tdiard
'''
import socket
import pickle
import os
import sys
import json
host, port = ('localhost',5566)
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#cd P:\Documents\NSI\eclipse\bomberman\main
resp = 0
class Test():
    def __init__(self,x,y,h):
        self.x = x
        self.y = y
        self.heading = h
        
    def calc(self,x,y):
        self.calc = x + y
        return self.calc

test = Test(5,5,3)
x,y = (test.x,test.y)
print(test.calc(x, y))
print(x,y)
msg = [5,2,["test"]]
print(msg)
#msg = msg.encode("utf8")
#print(msg)
msg = json.dumps(msg).encode("utf-8")
print(msg)

try: 
    ClientSocket.connect((host,port))
    print("Client connected !")
    
    ClientSocket.sendall(msg)
except:
    print("Connection Failed !")
finally:
    ClientSocket.close()
  