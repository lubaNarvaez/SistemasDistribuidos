import socket
from time import ctime 
import threading 

class Cliente(threading.Thread):
    def __init__(self,Addr):
        super(Cliente, self).__init__() 
        self.cliente=socket.socket() 
        self.cliente.connect(Addr) 

    def run(self):
        while True:
            data=input('>') 
            if not data:
                break 
            self.cliente.send(data.encode('utf-8')) 
            data=self.cliente.recv(1024) 
            if not data:
                break 
            print(data.decode('utf-8')) 

        self.cliente.close() 

if __name__ == '__main__':
    Cli=Cliente(('localhost', 8001));   #Generar un objeto de cliente
    Cli.start();
    