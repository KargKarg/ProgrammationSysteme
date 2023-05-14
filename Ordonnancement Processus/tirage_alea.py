import os
import random
import signal
import time

pool = []

for _ in range(10):
    fils = os.fork()

    if fils == 0:
        time.sleep(0.1)
        break

    else:
        os.kill(fils, signal.SIGSTOP)
        pool.append(fils)


if fils == 0:
    print(f'Coucou je suis {os.getpid()}')
    
else:
    while pool != []:
        proc = random.choice(pool)
        pool.remove(proc)

        os.kill(proc, signal.SIGCONT)

        os.wait()
