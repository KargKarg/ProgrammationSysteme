import os
import time
import signal

queue = []

for _ in range(100):
    fils = os.fork()
    if fils == 0:
        time.sleep(0.1)
        break
    else:
        os.kill(fils, signal.SIGSTOP)
        queue.append(fils)


if fils == 0:
    print(f'Coucou je suis le {os.getpid()}')

else:
    for process in queue:
        os.kill(process, signal.SIGCONT)
        os.wait()