n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))

total = (n1 + n2) + (n3 - n4)

if total <= 10:
    print("Resultado menor ou igual a dez")
else:
    print("Resultado maior que dez")