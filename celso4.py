g1 = []
g2 = []
mediaArtimetica = []

print('\n---------------------------------------------------------')
quantidadeAlunos = int(input('\nInforme a quantidade de alunos: '))

for y in range(1, quantidadeAlunos + 1):
    print('\n---------------------------------------------------------')
    nota1 = float(input(f'\nInforme a nota G1 do aluno {y}: '))
    g1.append(nota1)
    nota2 = float(input(f'\nInforme a nota G2 do aluno {y}: '))
    g2.append(nota2)
    media = (nota1 + nota2) / 2
    mediaArtimetica.append(media)

print('G1 é: ', g1)
print('G2 é: ', g2)
print('A média aritmética é: ', mediaArtimetica)