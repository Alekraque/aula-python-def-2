carros = ['up', 'uno', 'celta', 'gol', 'fusca']
precos = [10, 20, 100, 50, 15]
localMaior = 0
maior = precos[localMaior]
for i in range(len(precos)):
    if precos[i] > maior:
        maior = precos[i]
        localMaior = i
print(f'{carros[localMaior]} custa R${precos[localMaior]:.2f}')
