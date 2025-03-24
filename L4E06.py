a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

# ver se todos são iguais
if a == b:
    print(f"Os números são iguais: {a}")
# Se eles não forem iguais
else:
    if a < b:
        print(f"Números em ordem crescente: {a} e {b}")
    else:
        print(f"Números em ordem crescente: {b} e {a}")