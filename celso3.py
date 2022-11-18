vetorMedia = []
somaValoresDigitados = 0
somatorioTotal = 0

while True:
    numeros = float(
        input('Informe alguns números (quando quiser parar é só digitar "0"): ')
    )

    if numeros == 0:
        break

    vetorMedia.append(numeros)
    somaValoresDigitados= somaValoresDigitados + 1

for n in vetorMedia:
    somatorioTotal = somatorioTotal + n

mediaAritmetica = somatorioTotal  / somaValoresDigitados

print(f'A soma dos valores é: {somatorioTotal}')
print(f'O valor da média é: {mediaAritmetica} ')
