import threading
import random
import sys

tab = [random.randint(1, 100) for _ in range(100)]
nb_threads = 20
lock = threading.Lock()
taille_sous_tab = len(tab)//nb_threads

somme = 0
moyenne = 0
maximum = tab[0]
minimum = tab[0]

def somme_tab(tab, g, d):
    global somme
    sous_somme = 0
    for i in range(g, d):
        sous_somme += tab[i]
    lock.acquire()
    somme += sous_somme
    lock.release()
    print(f'Mon sous-tableau était {tab[g:d]} et ma somme était {sous_somme}, vérification avec sum(tab[g:d]) : {sum(tab[g:d])}')

def moyenne_tab(tab, g, d):
    global moyenne
    sous_moyenne = 0
    for i in range(g, d):
        sous_moyenne += tab[i]
    sous_moyenne /= (d-g)
    lock.acquire()
    moyenne += sous_moyenne
    lock.release()
    print(f'Mon sous-tableau était {tab[g:d]} et ma moyenne était {sous_moyenne}, vérification avec sum(tab[g:d])/(d-g) : {sum(tab[g:d])/(d-g)}')

def maximum_tab(tab, g, d):
    global maximum
    sous_maximum = tab[g]
    for i in range(g, d):
        if tab[i] > sous_maximum:
            sous_maximum = tab[i]
    if sous_maximum > maximum:
        lock.acquire()
        maximum = sous_maximum
        lock.release()
    print(f'Mon sous-tableau était {tab[g:d]} et mon maximum était {sous_maximum}, vérification avec max(tab[g:d]) : {max(tab[g:d])}')

def minimum_tab(tab, g, d):
    global minimum
    sous_minimum = tab[g]
    for i in range(g, d):
        if tab[i] < sous_minimum:
            sous_minimum = tab[i]
    if sous_minimum < minimum:
        lock.acquire()
        minimum = sous_minimum
        lock.release()
    print(f'Mon sous-tableau était {tab[g:d]} et mon minimum était {sous_minimum}, vérification avec min(tab[g:d]) : {min(tab[g:d])}')

def all_tab(tab, g, d):
    global somme, moyenne, maximum, minimum
    somme_tab(tab, g, d)
    moyenne_tab(tab, g, d)
    maximum_tab(tab, g, d)
    minimum_tab(tab, g, d)
    

if sys.argv[1] == '+':

    for i in range(0, len(tab), taille_sous_tab):
        t1 = threading.Thread(target=somme_tab, args=(tab, i, i+taille_sous_tab))
        t1.start()

    t1.join()

    print(f'\nLe tableau est {tab} et la somme est {somme}, vérification avec sum(tab) : {sum(tab)}')


elif sys.argv[1] == '/':

    for i in range(0, len(tab), taille_sous_tab):
        t2 = threading.Thread(target=moyenne_tab, args=(tab, i, i+taille_sous_tab))
        t2.start()

    t2.join()

    moyenne /= nb_threads

    print(f'\nLe tableau est {tab} et la moyenne est {round(moyenne, 2)}, vérification avec sum(tab)/len(tab) : {sum(tab)/len(tab)}')


elif sys.argv[1] == 'M':

    for i in range(0, len(tab), taille_sous_tab):
        t3 = threading.Thread(target=maximum_tab, args=(tab, i, i+taille_sous_tab))
        t3.start()

    t3.join()

    print(f'\nLe tableau est {tab} et le maximum est {maximum}, vérification avec max(tab) : {max(tab)}')


elif sys.argv[1] == 'm':

    for i in range(0, len(tab), taille_sous_tab):
        t4 = threading.Thread(target=minimum_tab, args=(tab, i, i+taille_sous_tab))
        t4.start()

    t4.join()

    print(f'\nLe tableau est {tab} et le minimum est {minimum}, vérification avec min(tab) : {min(tab)}')

elif sys.argv[1] == 'all':

    for i in range(0, len(tab), taille_sous_tab):
        t5 = threading.Thread(target=all_tab, args=(tab, i, i+taille_sous_tab))
        t5.start()

    t5.join()

    moyenne /= nb_threads

    print(f'\nLe tableau est {tab} et la somme est {somme}, vérification avec min(tab) : {min(tab)}')
    print(f'\nLa moyenne est {round(moyenne, 2)}, vérification avec sum(tab)/len(tab) : {sum(tab)/len(tab)}')
    print(f'\nLe maximum est {maximum}, vérification avec max(tab) : {max(tab)}')
    print(f'\nLe minimum est {minimum}, vérification avec min(tab) : {min(tab)}')