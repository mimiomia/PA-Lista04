a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

# Se forem iguais
if a == b:
  print("Os números são iguais")
else:
  if a > b:
    maior = a
    menor = b
  else:
    maior = b
    menor = a

  menor = menor * 10
  maior = maior / 2
  soma = menor + maior

  # Verificar se é par
  if soma % 2 == 0:
    print("O resultado é par")
  else:
    print("O resultado é ímpar")