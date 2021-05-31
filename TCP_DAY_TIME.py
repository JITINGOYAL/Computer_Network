// Server.py

import socket
import time
from threading import Thread 

def thread():
    while True:
        data = conn.recv(1024)
        print('Client Request :' + data.decode())
        if ('quit' in data.decode()) or not data:
            print("Server Exiting")
            conn.close()
            break
        elif('time' in data.decode()):
            st = time.asctime( time.localtime() )
            print ("Local current time :", st)
            conn.sendall(st.encode()) 
            continue
        else:
            print('Type your response:',end='')          
            st=input()
            conn.sendall(st.encode())  

host = '127.0.0.1'
port = 15000
s = socket.socket()     
s.bind((host,port))
s.listen(2)

print("Waiting for clients...")
while True:
    conn,addr = s.accept()          
    print("Connected by ", addr)
    pr = Thread(target=thread)
    pr.start()

conn.close()


// client.py

import socket
def client():
    
    s=socket.socket()
    
    host='127.0.0.1'
    port=15000
    s.connect((host,port))
    while(True):
        num=(input())
        if(num == 'quit'):
            s.close()
            break

        s.send(num.encode())
        data=s.recv(1024).decode()
        print('This is the response: '+ data)
        
client()

