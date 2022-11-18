salarios = [1500, 1350, 1200, 800, 900]
salariosAtualizados = []
for s in salarios:
    if s < 1000:
        novoValor= s+(s*0.10)
        salariosAtualizados.append(novoValor)
    if s > 1000:
        salariosAtualizados.append(s)

print(salariosAtualizados)