import os
import sys


fd = os.open(sys.argv[1], os.O_RDONLY)
fd_out = os.open(f"{sys.argv[2]}/{sys.argv[1]}", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

texte = ''
lecture = os.read(fd, 1).decode('utf-8')

while lecture != '':
    texte += lecture
    lecture = os.read(fd, 1).decode('utf-8')

os.write(fd_out, texte.encode('utf-8'))

os.close(fd)
os.close(fd_out)

os.unlink(sys.argv[1])
