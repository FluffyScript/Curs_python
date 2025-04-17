# Tema de casa

# Intrebam utilizatorul : "Cum este ziua ta?"
# Programul va raspunde in functie de raspuns:
#     - daca utilizatorul raspunde: "buna" sau "ok" sau "faina"
#          - atunci programul va raspunde cu "Foarte bine, ma bucur sa aud."
#     - daca utilizatorul raspunde: "rea" sau "neplacuta" sau "trista"
#          - atunci programul va raspunde cu "Nu iti face griji, te descurci perfect."
#     - daca utilizatorul raspunde: "as vrea o bere"
#          - atunci programul va raspunde cu "Nu, nu este bine sa bei alcool"
#     - daca utilizatorul raspunde: "as vrea sa invat programare"
#          - atunci programul va raspunde cu "Felicitari, ai castigat la viata!"

# Cerinta suplimentara pentru extra puncte
# *** Fa ca programul sa ruleze la infinit

# Exemplu de program simplu

input_tastatura = input("Cum este ziua ta?")
rezultat = 'lasa-ma in pace'

if input_tastatura == 'buna' or input_tastatura == 'ok' or input_tastatura == 'faina':
    rezultat = "Foarte bine, ma bucur sa aud."

print(rezultat)
