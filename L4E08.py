x = int(input("Digite um número: "))

if x <= 10:
    soma = 20
    x = x + soma
else:
    soma = 5
    x = x + soma

if x > 25:
    print(f"O número inserido somado a {soma} é igual a {x}")