#É uma função que permite que o usuário forneça informações a um programa. Ela exibe uma mensagem, aguarda a entrada do usuário e retorna o que o usuário digitou.
#O programa em si gera a resposta à maquina como string, é preciso fazer uma conversão ou cast

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:" ))
altura = float(input("Digite sua altura: "))

print(nome)
print(type(idade))
print(type(altura))