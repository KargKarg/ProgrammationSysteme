import os 
import time

fd_read, fd_write = os.pipe()
nb_process = 20

for _ in range(nb_process):
    fils = os.fork()

    if fils == 0:
        break
    else:
        os.mkfifo(f"tube_pere_to_{fils}")

if fils == 0:
    os.close(fd_read)
    os.write(fd_write, f"{os.getpid()} Coucou papa\n".encode('utf-8'))
    os.close(fd_write)
    time.sleep(3)
    fd = os.open(f"tube_pere_to_{os.getpid()}", os.O_RDONLY)

    texte = ''
    lecture = os.read(fd, 1).decode('utf-8')

    while lecture != '':
        texte += lecture
        lecture = os.read(fd, 1).decode('utf-8')

    print(f"Je suis {os.getpid()} et j'ai recu de mon pere <<<<{texte}>>>>\n")

    os.close(fd)

    os.remove(f"tube_pere_to_{os.getpid()}")

else:
    os.close(fd_write)

    ligne = ''
    lecture = os.read(fd_read, 1).decode('utf-8')

    while lecture != '':
        if lecture == '\n':
            id = ligne.split()[0]
            fd = os.open(f"tube_pere_to_{id}", os.O_WRONLY)
            os.write(fd, f"Je suis ton pere tu m'as envoye : <<{ligne[len(ligne.split()[0]):]}>> tu es {id}".encode('utf-8'))
            os.close(fd)
        else:
            ligne += lecture
        lecture = os.read(fd_read, 1).decode('utf-8')
    
