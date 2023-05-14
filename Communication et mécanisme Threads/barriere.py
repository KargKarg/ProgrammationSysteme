import threading
import time

condition = threading.Condition()
lock = threading.Lock()
nb_threads = 100
compteur = 0

def barriere():
    global compteur

    lock.acquire()
    compteur += 1
    lock.release()

    if compteur < nb_threads:
        print(f'J\'attend, le compteur est à {compteur}!')
        with condition:
            condition.wait()
        print('Je suis de nouveau là !')
    
    else:
        print(f'Je les réveille dans 5s, le compteur est à {compteur}')
        for i in range(5):
            time.sleep(1)
            print(f"{i+1}s")
        with condition:
            condition.notify_all()
        compteur = 0
    

for _ in range(nb_threads):
    t1 = threading.Thread(target=barriere)
    t1.start()

t1.join()

time.sleep(5)

for _ in range(nb_threads):
    t1 = threading.Thread(target=barriere)
    t1.start()