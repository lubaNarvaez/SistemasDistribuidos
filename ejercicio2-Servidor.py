import socket
from datetime import datetime, date, time, timedelta
import pickle

def Servidor():
    
    servidor = socket.socket()
    servidor.bind(('localhost', 8001))
    servidor.listen(1)
    lista = ['luba','123456']

     
    conexion, addr = servidor.accept()
    mensaje = conexion.recv(1024)
    dato = mensaje
    dato1 = pickle.loads(dato)
    print(dato1)
    print(dato1[0])

   
    if dato1[0] in lista and dato1[1] in lista:

        now = date.today()
        now2 = datetime.now()
        nowH = time(now2.hour, now2.minute, now2.second)
        print(' Bienvenido: {} \n Te conectaste desde : {} \n Por el puerto: {} \n Fecha: {} \n Hora: {}'.format(lista[0], addr[0], addr[1], now, nowH))
    else:
        print('Lumayo-plasma no te permite entrar aqui, solamente entran las divinas')
    conexion.close()
    servidor.close()

if __name__ == '__main__':
    Servidor()
    