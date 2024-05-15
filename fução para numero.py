
def checaNumero(msg, msg_erro):
    numero = input(msg)
    while not numero.isnumeric():
        print(msg_erro)
        numero = input(msg)
    return numero

checaNumero('diga a quantidade de garrafas: ',' quantidade deve ser um numero')
checaNumero('diga a sua idade: ',' idade deve ser um numero')



'''qnt = input('diga a quantidade de garrafas: ')
while not qnt.isnumeric():
    print('diga um numero.')
    qnt = input('diga a quantidade de garrafas: ')

idade = input('diga sua idade: ')
while not idade.isnumeric():
    print('diga um numero.')
    idade = input('diga sua idade: ')'''

