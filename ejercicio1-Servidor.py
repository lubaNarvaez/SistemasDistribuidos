import socket
from datetime import datetime, date, time, timedelta

def Servidor():
    
    servidor = socket.socket()
    servidor.bind(('localhost', 8001))
    servidor.listen(1)

 
    conexion, addr = servidor.accept()
    mensaje = conexion.recv(1024)
    now = date.today()
    now2 = datetime.now()
    nowH = time(now2.hour, now2.minute, now2.second)
    print(' Bienvenido: {} \n Te conectaste desde : {} \n Por el puerto: {} \n Fecha: {} \n Hora: {}'.format(mensaje.decode('utf-8'), addr[0], addr[1], now, nowH))
    conexion.close()
    servidor.close()

if __name__ == '__main__':
    Servidor()
    