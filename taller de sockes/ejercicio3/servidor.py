# Clase de servidor

import socket                 # Módulo de enchufe
from time import ctime       # Módulo de tiempo para imprimir tiempo
import threading             # Módulo de hilo

class Servidor(threading.Thread):
    def __init__(self, Addr):                        #Addr: dirección IP del servidor
        super(Servidor, self).__init__()                       # Hilo de inicialización
        self.servidor=socket.socket()           #AF_INET representa la generación de sockets orientados a la red, SOCK_STREAM representa el tipo TCP
        self.servidor.bind(Addr)                            # Vincula la dirección IP del servidor al socket
        self.servidor.listen(5)

    def run(self):                                            # Función de inicio de subprocesos múltiples, solo se puede llamar run ()
        while True:
            print("Esperando conexion...") 
            cliente, addr = self.servidor.accept()          #accept () Después de recibir la aplicación de conexión del cliente, la función cambiará el mensaje para abandonar el bus, tcpCliSock es el operador, addr es la dirección IP del cliente
            print('...conectado desde:',addr) 

            while True:
                data=cliente.recv(1024)            # El mensaje enviado desde el cliente se almacena en datos
                if not data:
                    break 
                cliente.send(str('['+ctime()+']  ').encode('utf-8')+data) # Envíe el mensaje enviado por el cliente al cliente y adjunte una marca de tiempo para indicar que el servidor lo recibió

            cliente.close()                                # Cerrar canal de operador
        self.servidor.close()                                    #Cerrar conexión TCP

if __name__ == '__main__':
    Ser=Servidor(('localhost', 8001))  #Generar un objeto de servidor
    Ser.start()

    
    
