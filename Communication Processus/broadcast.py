import os
import time

nb_proc = 20

for i in range(nb_proc):
    os.mkfifo(f'tube_pere_to_{i}')
    fils = os.fork()

    if fils == 0:
        time.sleep(0.8)
        break


if fils == 0:
    time.sleep(2)
    fd = os.open(f"tube_pere_to_{i}", os.O_RDONLY)

    texte = ''
    lecture = os.read(fd, 1).decode('utf-8')

    while lecture != '':
        texte += lecture
        lecture = os.read(fd, 1).decode('utf-8')
    
    os.close(fd)
    os.unlink(f"tube_pere_to_{i}")

    print(f"Je suis {os.getpid()} et j'ai reçu : {texte}")




else:
    for i in range(nb_proc):
        fd = os.open(f"tube_pere_to_{i}", os.O_WRONLY)
        os.write(fd, "Hello c'est papa !".encode('utf-8'))
        os.close(fd)

    for _ in range(nb_proc):
        os.wait()
    