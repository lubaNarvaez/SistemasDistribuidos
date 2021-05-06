import threading
import random
from math import sqrt


class MyThread(threading.Thread):
    def __init__(self, ori, des):
        super(MyThread, self).__init__()
        self.origen = ori
        self.destino= des
        self.suma_parcial=0

    def suma_rango(self,origen,destino):
        suma = pow(2, origen) + pow(2, destino)
        return suma
    
    def run(self):
        self.suma_parcial=self.suma_rango(self.origen,self.destino)

if __name__ == "__main__":
    
    vector = []
    for i in range(20):
        vector.append(random.randint(1, 100))
    suma=0
    ori=0
    des=2
    threads = []
    for i in range(10):

        t = MyThread(vector[ori],vector[ori+1])
        t.start()
        threads.append(t)
        ori=des
        des+=2
		
    for t in threads:
        t.join()
    for h in range(10):
        suma=suma+threads[h].suma_parcial
    suma = sqrt(suma)

    print "la norma del vector es: "+str(suma)