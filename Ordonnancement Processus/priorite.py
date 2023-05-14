import os
import signal
import random
import time

pool = []

for _ in range(50):

    degre = random.randint(1, 10)
    fils = os.fork()

    if fils == 0:
        time.sleep(0.2)
        break

    else:
        os.kill(fils, signal.SIGSTOP)
        for _ in range(degre):
            pool.append((fils, degre))

    
if not fils:
    print(f"Coucou je suis {os.getpid()} et mon degre est {degre}")
else:
    while pool != []:
        proc, degre = random.choice(pool)
        for _ in range(degre):
            pool.remove((proc, degre))
        os.kill(proc, signal.SIGCONT)
        os.wait()