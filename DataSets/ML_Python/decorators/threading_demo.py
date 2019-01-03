from threading import Thread 
class MyThread(Thread):
    def __init__(self, tname):
        Thread.__init__(self, name= tname)
    def run(self):
        for val in range(0,4):
            print("Inside Run func", self.getName() , val)


t1 = MyThread("First")
t1.start()

t2 = MyThread("Second")
t2.start()