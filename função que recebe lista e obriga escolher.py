#função qie recebe uma lista de opções, e obrigue o usuario a escolher uma opção valida


lista = ['civic', 'corolla', 'accord', 'palio']
def obrigar(msg, msgErro):
    carro = input(msg)
    for i in lista:
        while not carro in lista:
            print(msgErro)
            carro = input(msg)
    return carro
obrigar('escolha um carro: ', 'este carro não está na lista')
print('carro está na lista')
