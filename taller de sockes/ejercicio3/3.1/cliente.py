import socket  
 
cliente = socket.socket()   
cliente.connect(("localhost", 8001))
while True:
    data=input('>') 
    if not data:
        break 
    cliente.send(data.encode('utf-8')) 
cliente.close() 

    