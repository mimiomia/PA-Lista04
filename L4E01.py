a = int(input("Insira um número: "))
b = int(input("Insira outro número: "))

if a == b:
    print(f"Os números são iguais")
else:
    if a < b:
        print(f"O número {a} é o menor")
    else:
        print(f"O número {b} é o menor")
