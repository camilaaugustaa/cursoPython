#Calculadora básica

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

soma = number1 + number2
subtracao = number1 - number2
multiplicacao = number1 * number2
divisao = number1 / number2
exponenciacao = number1 ** number2
resto = number1 % number2

print(f"A soma dos números é: {soma}")
print(f"A subtração dos números é: {subtracao}")
print(f"A multiplicação dos números é: {multiplicacao}")
print(f"A divisão dos números é: {divisao}")
print(f"A exponenciação dos números é: {exponenciacao}")
print(f"O resto da divisão dos números é: {resto}")