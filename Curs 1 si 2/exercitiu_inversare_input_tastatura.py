import queue

# Introducere in variabile
variabila_booleana: bool = True # True -> este un tip de data primitiva
variabila_numerica: int = 23
variabila_numerica_2: float = 4.25
variabila_caracter: str = 'O'
variabila_sir_de_caractere: str = "Salutari"

# Re-atribuire de valori catre variabile deja definite
variabila_sir_de_caractere = "Papa"
variabila_sir_de_caractere = 10.45

# Lui print, ca functie, ii putem da ORICE tip de variabila
print(variabila_sir_de_caractere)

# Tipuri de date primitive:           Notati in python:
# boolean / bool : True, False        # bool
# Int, Double : 1, -15, -0.345        # int, float
# Caracter  : 'c', 'a', 'B'           # str
# Sir de caractere : "caB"            # str
# Tipurile declarate pentru o variabila pot fi monitorizate cand rulam aplicatia,
# acest lucru se face prin configurare compiler-ului
# Articol 'Medium' despre primitive in Python : https://medium.com/codex/primitive-data-type-in-python-c0bc8f5deaef




# # Partea de aplicatie
# Vrem sa citim de la tastatura un sir de caractere scris de utilizator (standard input)
# Aplicatia va inversa ce scrie utilizatorul si va afisa rezultatul

scris_utilizator = input('Enter your input:')

# exemplu:
# input = "Salutari"
# putem interpreta input ca : ['S', 'a', 'l', 'u', 't', 'a', 'r', 'i']



# ------ Rezolvare simpla (nu facem asa):
# rezultatul = scris_utilizator[::-1]
# print(rezultatul)   - 
# quit() # quit()     - este o functie care cand este apelata incheie programul



# ------ Rezolvarea complicata prin tipul de data 'coada'/'queue'
coadaLIFO = queue.LifoQueue()    # coada este un tip de data, o poti asocia cu o galeata
                                 # intr-o galeata, ce intra primul, iese ultimul
                                 # cozile sunt tipuri de date complexe, nu primitive

for caracter in scris_utilizator:
    # pentru tipurile de date complexe, odata ce apasam '.' dupa numele acestora, 
    # putem vedea ce functii sunt disponibile pentru acel tip de date
    coadaLIFO.put(caracter)

rezultat = []
while not coadaLIFO.empty():
    rezultat.append(coadaLIFO.get())

# for - este un operator care itereaza date de tip sir
# ** str este un tip de data care este sir, este un sir de caractere
rezultat_ca_sir_normal = ''.join(rezultat)
print(rezultat_ca_sir_normal)
