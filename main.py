'''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
for elem in range(len(numeros)):
    if numeros[elem]%2 == 0:
        pares.append(numeros[elem])
        continue
    impares.append(numeros)
print(numeros)
print(pares)


for i in numeros:
    if i %2 == 0:
        pares.append(i)
        continue
    impares.append(i)
print(numeros)
print(pares)'''


'''professores = ['cordeiro', 'danilo', 'lucas silva', 'lucas augusto', 'jones', 'ana claudia', 'caio oliveira']
materias = ['software design', 'python', 'front end', 'edge computing', 'matematica', 'storytelling', 'JavaScript']

for i in range(len(professores)):
    print(f'o prof {professores[i]} da aula de {materias[i]}')'''


professores = ['cordeiro', 'danilo', 'lucas silva', 'lucas augusto', 'jones', 'ana claudia', 'caio oliveira']
materias = ['software design', 'python', 'front end', 'edge computing', 'matematica', 'storytelling', 'JavaScript']
#peça ao usuario um professor de input, e verifique se esse professor está na lista. Se estiver,
#busque o local do professor na lista e depois printe o que o professor escolhido dá de materia
#e se o professor nao estiver na lista, mande ele digitar outro nome de professor.


'''escolha = input('diga um professor: ')
for i in range(len(professores)):
    while not escolha in professores:
        print('escolha outro professor')
        escolha = input('diga um professor: ')
    print(f'o prof {professores[i]} da aula de {materias[i]}')'''

#exercicio certo:
'''while True:
    nome = input('diga um professor: ')
    for i in range(len(professores)):
        if professores[i] == nome:
            print(f'o prof {nome} dá {materias[i]}')
            achou = True
            break'''

#outro jeito certo de fazer:
'''escolha = input('diga um professor: ')
while not escolha in professores:
    print('escolha outro professor')
    escolha = input('diga um professor: ')
for i in range(len(professores)):
    if professores[i] == escolha:
        print(f'o prof {professores[i]} da aula de {materias[i]}')'''






