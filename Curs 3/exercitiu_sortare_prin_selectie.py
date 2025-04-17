
# Definitie : sortare prin selectie
    # fie un vector X[] cu n elemente;
    # plasăm în X[0] cea mai mică valoare din vector;
    # plasăm în X[1] cea mai mică valoare rămasă;
    # etc.

# Cerinte:
# Citim un sir de la tastatura
# Il sortam prin selectie
# Afisam sirul sortat

# Pentru comparatie, asa arata algoritmul in C++
# int n, X[100];
# //citire X[] cu n elemente
# for(int i = 0 ; i < n - 1 ; i ++)
#     for(int j = i + 1 ; j < n ; j ++)
#         if(X[i] > X[j])
#         {
#             int aux = X[i];
#             X[i] = X[j];
#             X[j] = aux;
#         }

from random import randint
from timeit import default_timer as timer

# [ 0   1   2   3   4]
# [47, 23, 12, 17, 30]

def sortare_prin_selectie(sir: list):
    for valoare_poz_i in sir:
        index_i = sir.index(valoare_poz_i)
        ultimul_index = len(sir) - 1
        
        # Acest if face ca index_i sa sara peste 4 (ultimul)
        if index_i >= ultimul_index:
            continue
        
        # iteratia j a doua, s-a schimbat sirul, acum avem
        # [23, 47, 12, 17, 30]
        for valoare_pozitia_j in sir:
            index_j = sir.index(valoare_pozitia_j)

            # Acest if face ca index_j sa fie mereu mai mare decat index_i
            if index_j <= index_i:
                continue

            if sir[index_i] > sir[index_j]:
                auxiliar = sir[index_i]
                sir[index_i] = sir[index_j]
                sir[index_j] = auxiliar

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
    print('SORTARE PRIN SELECTIE: ')
    for numar in sir:
        print(numar)


sir_de_numere = []
for i in range(1, 999):
    numar = randint(99, 9999999)
    sir_de_numere.append(numar)

#sir_de_numere = [47, 12, 30, 6, 45, 3, 17, 4, 10, 9, 5] #citire_tastatura()

inceput = timer()
sir_sortat = sortare_prin_selectie(sir_de_numere)
final = timer()

timp_final = final - inceput 
print('SORTARE PRIN SELECTIE: ')
print(f'Timpul de executie al algoritmului este : {timp_final}')

# afisare_sir(sir_sortat)
