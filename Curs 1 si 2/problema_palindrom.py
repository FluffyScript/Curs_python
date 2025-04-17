import queue

# Problema: 
# - dorim sa citim de la tastatura un numar
# - aplicatia va detecta daca numarul este un palindrom
# - aceasta va afisa adevarat sau fals in functie de situatie

## Un palindrom este un numar care citit de la coada la cap este acelasi numar daca l-am citi de la cap la coada
## Exemple de numere care nu sunt palindrom : 1241211, 12312545, 098
## Studiu de caz pentru numarul 1241211: 
##                      de la cap la coada: 1241211
##                      de la coada la cap: 1121421
##                      cele doua numere NU sunt egale, prin urmare, numarul NU este palindrom
##
## Exemple de numere care sunt palindrom : 12321, 555, 1
## Studiu de caz pentru numarul 1241211: 
##                      de la cap la coada: 12321
##                      de la coada la cap: 12321
##                      cele doua numere sunt egale, prin urmare, numarul ESTE palindrom

numar_tastatura = input('Enter your input:')
este_numarul_palindrom = False

# Rezolvarea problemei

print(este_numarul_palindrom)
quit() # iesire din aplicatie



# ------ Rezolvarea problemei anterioare
# ------ # inversarea unui sir de caractere
coadaLIFO = queue.LifoQueue()    

for caracter in numar_tastatura:
    coadaLIFO.put(caracter)

rezultat = []
while not coadaLIFO.empty():
    rezultat.append(coadaLIFO.get())

rezultat_ca_sir_normal = ''.join(rezultat)
print(rezultat_ca_sir_normal)
