# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    resultado = abs(num1 + num2)
elif operacao == "-":
    resultado = abs(num1 - num2)
elif operacao == "*":
    resultado = abs(num1 * num2)
elif operacao == "/":
    resultado = abs(num1 / num2)
else:
    resultado = "Operação inválida"

print("O resultado da operação é:", resultado)