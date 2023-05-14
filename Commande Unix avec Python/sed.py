import os
import sys


fd = os.open(sys.argv[1], os.O_RDONLY)

texte = ''
lecture = os.read(fd, 1).decode('utf-8')

while lecture != '':
    texte += lecture
    lecture = os.read(fd, 1).decode('utf-8')

os.close(fd)

texte = texte.replace(sys.argv[2], sys.argv[3])

fd = os.open(sys.argv[1], os.O_WRONLY | os.O_TRUNC)

os.write(fd, texte.encode('utf-8'))

os.close(fd)

