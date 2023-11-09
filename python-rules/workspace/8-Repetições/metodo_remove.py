lista_cores = ['vermelho', 'azul', 'verde', 'vermelho', 'amarelo']

# Removendo a cor na posição 2 usando pop
cor_removida = lista_cores.pop(2)

# Imprimindo a lista após a remoção
print(f"Cor removida: {cor_removida}")
print("Lista após a remoção:", lista_cores)


#Neste exemplo, lista_cores.remove('vermelho') remove a primeira ocorrência da string 'vermelho' da lista. A lista é então impressa para mostrar o resultado após a remoção. Se o item não estiver na lista, o método remove gerará uma exceção ValueError, então é sempre uma boa prática verificar se o item está na lista antes de chamar o método remove.
#Lista após a remoção: ['azul', 'verde', 'vermelho', 'amarelo']

#Cor removida: verde
#Lista após a remoção: ['vermelho', 'azul', 'vermelho', 'amarelo']
