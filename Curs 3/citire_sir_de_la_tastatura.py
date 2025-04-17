sir = []

# citire
print('Se citeste un sir de la tastatura. \n Pentru a termina citirea, apasati \'X\'. \n ')
numar_nou = input('Introduceti urmatorul element:')
while numar_nou != 'x':
    sir.append(numar_nou)
    numar_nou = input('Introduceti urmatorul element:')

# afisare
print('Sirul citit este: ')
for numar in sir:
    print(numar)

input('\n\nApasati tasta Enter pentru a iesi din program.')