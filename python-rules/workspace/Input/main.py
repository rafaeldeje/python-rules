#Aprenderemos hoje sobre a função INPUT onde a maquina pede ao usuario uma resposta para o programa,
#O programa em si gera a resposta à maquina como string, é preciso fazer uma conversão ou cast

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:" ))
altura = float(input("Digite sua altura: "))

print(nome)
print(type(idade))
print(type(altura))