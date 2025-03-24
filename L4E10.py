#Crie um algoritmo que leia dois números
# multiplique o menor por 10,
# e divida o maior por 2,
# some os seus valores e 
# verifique se o resultado e par,
# em caso afirmativo exiba a mensagem, o resultado é par, caso contrario, exiba a mensagem, o resultado é impar. 

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

# Se forem iguais
if a == b:
  print("Os números são iguais")

if a > 10:
  b = b * 10
  a = a / 2
  soma = a + b
  # Verificar se é par
  if total % 2 == 0:
    print("O resultado é par")
  else:
    print("O resultado é ímpar")

else:
  a = a * 10
  b = b / 2
  soma = a + b
  # Verificar se é par
  if total % 2 == 0:
    print("O resultado é par")
  else:
    print("O resultado é ímpar")
  
