## Python TCP Client B
import socket 
import time
import random
host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2000 

count=0
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

#while MESSAGE != 'exit':
file1 = open('./send_file2.txt', 'r') 
Lines = file1.readlines() 
print (">>>>>>>",len(Lines))
count = 0
MESSAGE=''
for line in Lines: 
    MESSAGE= "data_sentby_B"+"  "+line.strip()
    MESSAGE=MESSAGE.encode()
    tcpClientA.send(MESSAGE)     
    data = tcpClientA.recv(BUFFER_SIZE)
    print (" ClientA received data:", data)
    time.sleep(0.002)
# MESSAGE='end of data B'
# MESSAGE=MESSAGE.encode()
# tcpClientA.send(MESSAGE) 
tcpClientA.close() 
print("end of data")