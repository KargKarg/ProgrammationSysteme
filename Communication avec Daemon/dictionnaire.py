import threading
import os

launch = True

def dictionnaire():
    global launch
    dico = {}

    while launch:
        action = input(f'\nQue voulez vous faire ?'\
                    '\nADD key val => Ajoute une clé et valeur dans le dictionnaire'\
                    '\nDEL key => Supprime la clé du dictionnaire'\
                    '\nSHOW key => Affiche la valeur d\'une clé'\
                    '\nSHOWALL => Affiche tout le dictionnaire'\
                    '\nRESET => Réinitialise le dictionnaire'\
                    '\nSAVE path => Enregistre le dictionnaire sous format .txt : clé valeur'\
                    '\nQUIT => Termine le programme\n').split()
        
        if action[0].upper() == 'ADD':
            dico[action[1]] = action[2]
        
        elif action[0].upper() == 'DEL':
            del dico[action[1]]

        elif action[0].upper() == 'SHOW':
            print(dico[action[1]])
        
        elif action[0].upper() == 'SHOWALL':
            print(dico)

        elif action[0].upper() == 'RESET':
            dico = {}

        elif action[0].upper() == 'SAVE':
            fd = os.open(f"{action[1]}.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
            for key, val in dico.items():
                os.write(fd, f"{key} {val}\n".encode('utf-8'))
            os.close(fd)
        
        elif action[0].upper() == 'QUIT':
            launch = False

daemon = threading.Thread(target=dictionnaire, daemon=True)
daemon.start()

while launch:
    pass