import os

for fichier in os.listdir():
    meta = os.stat(fichier)
    print(f"{meta.st_mode} {meta.st_uid} {meta.st_size} {meta.st_atime} {fichier}")