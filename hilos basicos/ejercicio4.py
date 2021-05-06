import threading
from math import factorial
#import time

class MyThread(threading.Thread):
    def __init__(self, ori,des):
        super(MyThread, self).__init__()
        self.origen = ori
        self.destino= des
        self.suma_parcial=0

    def suma_rango(self,origen,destino):
        suma = 0
        while origen <= destino:
            suma = factorial(origen) + suma
            origen += 1
        return suma
    
    def run(self):
        self.suma_parcial=self.suma_rango(self.origen,self.destino)

if __name__ == "__main__":
    
    suma=0
    print 'Escriba el numero n: '
    n = input()
    print 'Escriba la cantidad de hilos: '
    h = input()
    div = n/h
    mod = n % h
    print mod
    ori=1
    des=div
    threads = []
    if mod == 0:
        for i in range(h):
            
            t = MyThread(ori,des)
            t.start()
            threads.append(t)
            ori=des+1
            des+=div
    else:
        for i in range(h-1): 
            t = MyThread(ori,des)
            t.start()
            threads.append(t)
            ori=des+1
            des+=div
        t = MyThread(ori,des+mod)
        t.start()
        threads.append(t)

        
		
    for t in threads:
        t.join()
    for h in range(h):
        suma=suma+threads[h].suma_parcial
    print "la suma total: "+str(suma)