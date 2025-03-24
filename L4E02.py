a = int(input("Insira um número: "))
b = int(input("Insira outro número: "))

if a == b:
    print("Os números são iguais e não temos um número menor para somar 5")
else:
    if a < b:
        a = a + 5
    else:
        b = b + 5

    if a == b:
        print("Os números se igualaram após a soma de 5 ao menor deles")
    else:
        if a > b:
            print(f"O {a} é o maior número")
        else:
            print(f"O {b} é o maior número")
