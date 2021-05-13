# Clase de servidor
import socket                 
import threading    

CLIENTES = []


class Cliente(threading.Thread):
    def __init__(self, conexion, direccion):                       
        super(Cliente, self).__init__()                      
        self.conexion = conexion          
        self.direccion = direccion 

    def difusion(self, datos):
        for cliente in CLIENTES:
            if cliente.conexion != self.conexion:
                cliente.conexion.sendall(datos)                           

    def run(self):   
        print('...conectado desde:',self.direccion) 
        while True:
            datos=self.conexion.recv(1024)       
            if not datos:
                print('no hay datos adios')
                break
            print(datos)
            self.difusion(datos)
             
        print('...Desconectado cliente:',self.direccion) 
        self.conexion.close()


class Servidor():
    def __init__(self, ip, puerto):
        self.ip = ip
        self.puerto = puerto
        self.servidor = None

    def crearSocket(self):
        self.servidor = socket.socket()
        self.servidor.bind((self.ip, self.puerto))
        self.servidor.listen(5)
    
    def iniciarSocket(self):
        self.crearSocket()
        print ("Servidor arriba, pero triste porque no tengo conexiones. pero sigo escuchando!!!...")
        while True:
            conexion, direccion = self.servidor.accept()
            cliente = Cliente(conexion, direccion)
            cliente.start()
            CLIENTES.append(cliente)

        for t in CLIENTES:
            t.join()

        self.servidor.close() 


if __name__ == '__main__':

    servidor = Servidor('localhost', 8001)  
    servidor.iniciarSocket()
     

    
    
