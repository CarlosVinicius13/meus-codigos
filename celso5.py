somaVetor = []
diferencaVetor = []
produtoVetor = []
divisaoVetor = []

print('\n---------------------------------------------------------')
question = input('Informe 5 números separados por vírgula: ')
vet1 = []
for n in question.split(','):
    if n.isdigit():
        vet1.append(int(n))

print('\n---------------------------------------------------------')
question2 = input('Informe outros 5 números separados por vírgula: ')
vet2 = [int(n) for n in question2.split(',') if n.isdigit()]

for n, y in zip(vet1, vet2):
    soma = n+y
    diferenca = n-y
    produto = n*y
    divisao = n/y
    somaVetor.append(soma)
    diferencaVetor.append(diferenca)
    produtoVetor.append(produto)
    divisaoVetor.append(divisao)

print('soma: ', somaVetor)
print('diferença: ', diferencaVetor)
print('produto: ', produtoVetor)
print('divisão: ', divisaoVetor)