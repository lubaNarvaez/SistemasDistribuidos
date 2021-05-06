import threading
#import time

class MyThread(threading.Thread):
    def __init__(self, num1, num2, op):
        super(MyThread, self).__init__()
        self.num1 = num1
        self.num2= num2
        self.resultado=0
        self.op = op

    def sumar(self,num1,num2):
        return num1 + num2
    
    def restar(self,num1,num2):
        return num1 - num2

    def multi(self,num1,num2):
        return num1 * num2

    def div(self,num1,num2):
        return num1 / num2
    
    def run(self):
        if self.op == 0:
            self.resultado=self.sumar(self.num1,self.num2)
        elif self.op == 1:
            self.resultado=self.restar(self.num1,self.num2)
        elif self.op == 2:
            self.resultado=self.multi(self.num1,self.num2)
        elif self.op == 3:
            self.resultado=self.div(self.num1,self.num2)

                

if __name__ == "__main__":
    
    num1=5
    num2=3
    threads = []
    for i in range(4):
        
        t = MyThread(num1,num2,i)
        t.start()
        threads.append(t)
		
    for t in threads:
        t.join()
    for h in range(4):
        print "la operacion"+str(h)+" tiene resultado: "+str(threads[h].resultado)