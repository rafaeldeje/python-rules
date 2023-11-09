lista_frutas = ['maçã', 'banana', 'laranja', 'morango']

# Encontrando a posição da primeira ocorrência de 'laranja'
posicao_laranja = lista_frutas.index('laranja')

# Imprimindo a posição encontrada
print(f"A posição da primeira ocorrência de 'laranja' é: {posicao_laranja}")

#Neste exemplo, lista_frutas.index('laranja') retorna a posição da primeira ocorrência da string 'laranja' na lista. A posição é então impressa na tela. Se o item não estiver na lista, o método index irá gerar uma exceção ValueError, então é sempre uma boa prática verificar se o item está na lista antes de chamar o método index. 0 maca, 1 banana, 2 laranja, 3 morango