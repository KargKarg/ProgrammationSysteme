import os

fd_read, fd_write = os.pipe()
nb_process = 20

for _ in range(nb_process):
    fils = os.fork()
    if fils == 0:
        break


if fils == 0:
    os.write(fd_write, f"{os.getpid()} Coucou papa, je te passe le bonjour !\n".encode('utf-8'))
    os.close(fd_read)
    os.close(fd_write)

else:
    os.close(fd_write)

    ligne = ''
    lecture = os.read(fd_read, 1).decode('utf-8')

    while lecture != '':
        if lecture == '\n':
            print(f"J'ai recu de {ligne.split()[0]} : {ligne[len(ligne.split()[0]):]}")
            ligne = ''
        else:
            ligne += lecture
        lecture = os.read(fd_read, 1).decode('utf-8')
    
    os.close(fd_read)
