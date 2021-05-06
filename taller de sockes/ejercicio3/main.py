from servidor import Servidor;
from cliente import Client;
import threading;

from socket import *;
from time import ctime;


server_Host='';                       # Dirección del servidor, ya que estamos simulando la comunicación del cliente y el servidor en la misma computadora, no hay necesidad de completar la dirección del servidor
server_Port=21567;                    # Número de puerto del servidor, lo mejor es elegir un número de puerto no conocido
server_BufSize=1024;                  # Tamaño del búfer, la unidad es byte
server_Addr=(server_Host,server_Port);#Generar dirección del servidor, dirección del host más número de puerto

client_Host='localhost';              # El cliente es similar, ya no comenta, localhost se refiere a 127.0.0.1, también puede escribir directamente 127.0.0.1, esto se refiere a la dirección IP local,
client_Port=21567;
client_Bufsize=1024;
client_Addr=(client_Host,client_Port);

Ser=_Server(server_Addr, server_BufSize);  #Generar un objeto de servidor
Cli=_Client(client_Addr,client_Bufsize);   #Generar un objeto de cliente

#Multithreaded corriendo simultáneamente
Cli.start();
Ser.start();