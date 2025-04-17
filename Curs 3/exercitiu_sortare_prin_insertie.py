
# Definitie : sortare prin insertie
# Sortarea prin inserție (Insertion Sort) se bazează pe următoarea idee:
    # fie un vector X[] cu n elemente;
    # dacă secvența cu indici 0, 1, …, i-1 este ordonată, atunci putem insera elementul X[i] în această secvență astfel încât să fie ordonată secvența cu indici 0, 1, …, i-1, i.
    # luăm pe rând fiecare element X[i] și îl inserăm în secvența din stânga sa
    # la final întreg vectorul va fi ordonat

# Algoritm
# O reprezentare a algoritmului este:
    # parcurgem vectorul cu indicele i
    # inserăm pe X[i] în secvența din stânga sa; pentru inserare se mută unele elemente din secvență spre dreapta

# Cerinte:
# Citim un sir de la tastatura
# Il sortam prin insertie
# Afisam sirul sortat

# [ 0   1   2   3   4]
# [47, 23, 12, 17, 30]

from random import randint
from timeit import default_timer as timer

print("Otilia a fost aici")
def insertionSort(sir):
    lungime_sir = len(sir)  # Get the length of the array
     
    if lungime_sir <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    indexi = range(1, lungime_sir) # range - genereaza un sir de indexi pentru sirul nostru de numere, pornind de la 1 (primul parametru)
    for index in indexi: 
        valoare_sir_i = sir[index]  

        index_j = index-1
        while index_j >= 0 and valoare_sir_i < sir[index_j]: 
            sir[index_j+1] = sir[index_j]  # Shift elements to the right
            index_j -= 1
        sir[index_j+1] = valoare_sir_i 

    return sir
 
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
    for numar in sir:
        print(numar)



sir_de_numere = []
for i in range(1, 999):
    numar = randint(99, 9999999)
    sir_de_numere.append(numar)

# sir_de_numere = [47, 12, 30, 6, 45, 3, 17, 4, 10, 9, 5] #citire_tastatura()

inceput = timer()
sir_sortat = insertionSort(sir_de_numere)
final = timer()

timp_final = final - inceput 
print('SORTARE PRIN INSERTIE: ')
print(f'Timpul de executie al algoritmului este : {timp_final}')

# afisare_sir(sir_sortat)
