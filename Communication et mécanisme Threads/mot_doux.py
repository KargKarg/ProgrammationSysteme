import threading
import random


nb_threads = 20
message = ['' for _ in range(nb_threads)]
message[0] = random.randint(1, 100)


def transmission(indice):
    global message

    if indice == len(message)-1:
        print(f'Je suis le dernier et mon message est {message[indice]}')
    else:
        message[indice+1] = message[indice]
        print(message)


for i in range(nb_threads):
    t1 = threading.Thread(target=transmission, args=(i,))
    t1.start()
t1.join()