import threading
#import time

class MyThread(threading.Thread):
    def __init__(self, ori,des):
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
    
    suma=0
    ori=1
    des=2
    threads = []
    for i in range(5):
        
        t = MyThread(ori,des)
        t.start()
        threads.append(t)
        ori=des+1
        des+=2
		
    for t in threads:
        t.join()
    for h in range(5):
        suma=suma+threads[h].suma_parcial
    print "la suma total: "+str(suma)