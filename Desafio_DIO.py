# Gerar um código aleatório para cada pessoa cadastrada, como se fosse uma matrícula, contendo nome idade e cidade

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
matricula = nome[:2].upper() + str(idade) + cidade[-2:].upper()

print("Sua matrícula é:", matricula)