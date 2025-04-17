
# Terminologie
# a sorta - este un proces, o actiune pe care o facem pentru a stabili o ordine
# ordonat - este un atribut, o stare

# Definim functia de sortare cu numele 'bubble_sort'
# Parametrul 'sir' este ceva ce primim cand se apeleaza functia bubble_sort
# O metoda isi defineste propriul context / scop, adica
#     Variabilele pe care le declaram intr-o functie, traiesc doar in aceea functie, nu si in afra ei


# Cerinte:
# Sortare - inseamna ordonarea elementelor dintr-un sir pe baza unor criterii
# In acest exercitiu vom sorta un sir de numere in ordine crescatoare prin metoda bulelor

from random import randint
from timeit import default_timer as timer

def bubble_sort_crescator(sir: list):
    while True:  # avem o bucla infinita, se va repeta ce e indentat la dreapta la infinit
        presupunem_sortat = True
        
        # 'element_urmator' si 'numar' sunt variabile care reprezint un numar
        # in schimb!
        # sir[index_curent]     (care are valoare numar)         se refera la sir
        # sir[index_curent + 1] (care are valoare numar_urmator) se refera la sir
        for numar in sir:
            index_curent = sir.index(numar)
            ultimul_index = len(sir) - 1

            if index_curent < ultimul_index:
                element_urmator = sir[index_curent + 1] # retinem valoarea elementului urmator

                # elementele vecine nu sunt ordonate crescator, deci le inversam
                if numar > element_urmator:
                    auxiliar = sir[index_curent]
                    sir[index_curent] = element_urmator
                    sir[index_curent + 1] = auxiliar
                    presupunem_sortat = False
        
        if presupunem_sortat:
            # break va sparge structura de control while True de la linia 17
            break 
    return sir

def bubble_sort2(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False  

        for i in range(n):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break

def citire_tastatura():
    sir_de_numere = []
    # citire
    string_tastatura = input('Introduceti urmatorul element:')
    
    while string_tastatura != 'x' and string_tastatura != 'X':
        numar_nou = int(string_tastatura)
        sir_de_numere.append(numar_nou)
        string_tastatura = input('Introduceti urmatorul element:')
    
    # cand se apeleaza 'return', se iese din functie imediat!
    # dupa 'return' se poate scrie numele unei variabile (declarate in functie, desigur)
    #           Daca facem aceasta, se va trimite in afara functiei variabila in cauza
    return sir_de_numere

def afisare_sir(sir):
    print('BUBBLE SORT: ')
    for numar in sir:
        print(numar)

sir_de_numere = []
for i in range(1, 999):
    numar = randint(99, 9999999)
    sir_de_numere.append(numar)


# sir_de_numere = citire_tastatura()

# Sortarea sirului prin bubble sort

inceput = timer()
sir_sortat = bubble_sort_crescator(sir_de_numere)
final = timer()

timp_final = final - inceput 
print('BUBBLE SORT: ')
print(f'Timpul de executie al algoritmului este : {timp_final}')

# sir initial      : [13, 2, 5, 27, 3, 0]
# sortat crescator : [0, 2, 3, 5, 13, 27]
# afisare_sir(sir_sortat)
