salarios = []
mai = 0
men = 0
for s in range(0,2):
    salarios.append(float(input(f'Digite o salario: {s} ')))
    if s == 0:
        mai = men = salarios[s]
    else:
        if salarios[s] > mai:
            mai = salarios[s]
print("=-" * 30)
print(f"o maior salario é: {mai} ")