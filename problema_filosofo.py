import sys
import threading
import time


class Semaphore(object):

    def __init__(self, initial): #Función de Inicio
        #El self accede a los atributos y metodos de la clase
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self): #Función que levanta el tenedor
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self): #Función deja el tenedor
        with self.lock:
            while self.value==0:
                self.lock.wait()
            self.value -= 1


class forks(object):

    def __init__(self, number):
        self.number = number         # ID del tenedor
        self.user = -1               # Lleva el rastreo del filosofo usandolo
        self.lock = threading.Condition(threading.Lock())
        self. taken = False

    def take(self, user):               # Funcion de tomar el tenedor
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("Filosofo[%s] toma el tenedor:%s\n" % # Imprime en pantalla
                            (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):               # Funcion de dejar el tenedor
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("Filosofo[%s] deja el tenedor:%s\n" %
                                (user, self.number))
            self.lock.notifyAll()


class Philosopher (threading.Thread): #Clase filosofo por medio de hilos

    def __init__(self, number, left, right, butler):
        threading.Thread.__init__(self)
        self.number = number            #Numero Filosofo
        self.left = left
        self.right = right
        self.butler = butler

    def run(self):
        for i in range(1):
            self.butler.down()              #Empieza el servicio
            print("Filósofo", self.number, "piensa") 
            time.sleep(0.1)                 #Piensa
            self.left.take(self.number)     #Recoge el tenedor izquierdo
            time.sleep(0.1)
            self.right.take(self.number)    #Recoge el tenedor derecho
            print("Filósofo", self.number, "come")
            time.sleep(0.1)                 #Come
            self.right.drop(self.number)    #Deja el tenedor derecho
            self.left.drop(self.number)     #Deja el tenedor izquierdo
            self.butler.up()                #Termina el servicio
        sys.stdout.write(
            "Filosofo[%s] termina de pensar y comer\n" % self.number)


def main():
    # Numero de filosofos y tenedores
    n = 6

    #Butler para evitar el tiempo muerto deadlock
    butler = Semaphore(n-1)

    #Lista de tenedores
    c = [forks(i) for i in range(n)]

    #Lista de filosofos
    p = [Philosopher(i, c[i], c[(i+1) % n], butler) for i in range(n)]

    for i in  range (n):
        p[i].start()

if __name__ == "__main__":
    main()