#!/usr/bin/env python3
import socket  
from _thread import *
import threading 
  
print_lock = threading.Lock() 
def threaded(c): 
    data = ''
    buf = b''
    while True: 
        #print('Server: ')
        data = str(c.recv(4096).decode('ascii')) 
        print('Client :', data)
        if not data: 
            print('Bye') 
            print_lock.release() 
            break

        if data == 'bye':
            c.close()
            print('Bye bye')
            print_lock.release()
            break
        data = input('Server : ')
        c.send(data.encode('ascii')) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
    port = 12358
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("Socket binded to port:", port) 
  
    s.listen(5) 
    print("Connection Established") 
   
    while True: 
        c, addr = s.accept() 

        print_lock.acquire() 
        # print('Connected to :', addr[0], ':', addr[1]) 

        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 