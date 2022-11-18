salarios = [1350.6, 1420.6, 1421.6, 1500.50, 1210.50, 1500.65, 3010.52, 2150.50, 1250.50, 1350,65 ]

max_value = None

for s in salarios:
    if (max_value is None or s > max_value):
        max_value = s

print('Valor maximo = ', max_value)