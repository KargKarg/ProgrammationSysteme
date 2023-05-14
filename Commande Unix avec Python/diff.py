import os
import sys

fd_A = os.open(sys.argv[1], os.O_RDONLY)
fd_B = os.open(sys.argv[2], os.O_RDONLY)

texte_A = ''
lecture = os.read(fd_A, 1).decode('utf-8')

while lecture != '':
    texte_A += lecture
    lecture = os.read(fd_A, 1).decode('utf-8')

texte_B = ''
lecture = os.read(fd_B, 1).decode('utf-8')

while lecture != '':
    texte_B += lecture
    lecture = os.read(fd_B, 1).decode('utf-8')

for i in range(min(len(texte_A), len(texte_B))):
    if texte_A[i] != texte_B[i]:
        print(f"{texte_A[i]} différent de {texte_B[i]}")

os.close(fd_A)
os.close(fd_B)