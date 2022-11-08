import random
n1 = str(input("primeiro aluno "))
n2 = str(input("segundo aluno "))
n3 = str(input("terceiro aluno "))
n4 = str(input("quarto aluno "))
n5 = str(input("quinto aluno "))
lista = [n1, n2, n3, n4 ,n5]
random.shuffle(lista)
print("a ordem das apostas será ")
print(lista)