#Loop que percorre sequencias, repetindo acoes para cada elemento, faz uma repetição com um numero de repeticoes definidas.


notas = []

for x in range (5):
    codigo_aluno = input("RM: ")
    nota = float (input("Nota: "))
    resultado = (codigo_aluno, nota)
    notas.append(resultado)
