import socket 
import select
import sys
 
cliente = socket.socket()   
cliente.connect(('localhost', 8001))
inout = [sys.stdin, cliente]

while True:

    lectura, escritura, errores = select.select(inout, [], [])

    for socks in lectura:
        if socks == cliente:
            respuesta = cliente.recv(1024)
            print("Mensaje recibido: "+respuesta.decode('utf-8'))
        else:
            data = sys.stdin.readline()
            if not data:
                break 
            cliente.sendall(data.encode('utf-8'))
            sys.stdout.flush()  

cliente.close() 

    