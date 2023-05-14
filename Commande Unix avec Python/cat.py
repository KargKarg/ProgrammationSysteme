import os
import sys

fd = os.open(sys.argv[1], os.O_RDONLY)

ligne = ''
lecture = os.read(fd, 1).decode('utf-8')

while lecture != '':
    if lecture == '\n':
        print(ligne)
        ligne = ''
    else:
        ligne += lecture
    lecture = os.read(fd, 1).decode('utf-8')


os.close(fd)