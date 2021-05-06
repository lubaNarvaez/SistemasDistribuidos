import socket
import datetime

def Cliente():
    cliente = socket.socket()
    cliente.connect(('localhost', 8001))

    nombre = input('Ingrese su nombre: ')
    cliente.sendall(nombre.encode('utf-8'))
    cliente.close()

if __name__ == '__main__':
    Cliente()
    