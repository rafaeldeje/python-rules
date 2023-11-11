def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Digite o valor 1:"))
    valor2 = int(input("Digite o valor2: "))

    resposta = minha_funcao(valor1, valor2)
    print("resposta", resposta)
