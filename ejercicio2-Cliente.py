import socket
import datetime
import pickle


def Cliente():
    cliente = socket.socket()
    cliente.connect(('localhost', 8001))

    nombre = input('Ingrese su nombre: ')
    contraseña = input('Ingrese su contraseña: ')
    lista = [nombre, contraseña]
    datos = pickle.dumps(lista)
    cliente.sendall(datos)
    cliente.close()

if __name__ == '__main__':
    Cliente()
    