#!/usr/bin/env python3
import socket 
def Main(): 
    host = '127.0.0.1'
  
    port = 12358
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 

    sep = ''
    print('Send \"bye\" to exit conversation')
    s.send('Default Hello'.encode('ascii'))
    
    while True: 
  

        try:
            data = s.recv(4096) 
            print('Server :',str(data.decode('ascii'))) 
        except socket.error:
            #nothing recieved
            print('')

        message = input('Client : ')
        s.send(message.encode('ascii')) 
  
        if message == 'bye': 
            s.close()
            break
        else: 
            continue
    s.close() 
if __name__ == '__main__': 
    Main() 
