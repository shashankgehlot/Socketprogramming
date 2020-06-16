# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:25:45 2020

@author: shanks
"""
import os
import socket
import sys
from _thread import *
import threading
from collections import defaultdict
from re import search

#print_lock = threading.Lock()
path_of_data_storage="./recieved_data"
host = ''
port = 2004
count=1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
collections=defaultdict(list)
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection.')
def threaded_client(conn):
    conn.send(str.encode('server is reciving data from client\n'))
    global collections
    collections[conn].append(addr[1])
    while True:
        data = conn.recv(2048)
        if data:
            Data=data.decode()
            if not os.path.exists(path_of_data_storage):
                os.makedirs(path_of_data_storage)
            if os.path.exists(path_of_data_storage+"/recieved_data.txt"):
                f=open(path_of_data_storage+"/recieved_data.txt","a+")
                f.write("%s\r\n"%str(data.decode()))
                f.close()
            else:
                f=open(path_of_data_storage+"/recieved_data.txt","w+")
                f.write("%s\r\n"%str(data.decode()))
                f.close()   
        reply = 'Server output: '+ data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
        
    conn.close()

while True:
    conn, addr = s.accept()
    print ("Multithreaded Python server : Waiting for connections from TCP clients...")
    print('connected to: '+addr[0]+':'+str(addr[1])) 
    collections[conn]=[]
    data=0
    start_new_thread(threaded_client,(conn,))
   
    