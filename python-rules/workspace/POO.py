class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

# Criar uma instância da classe Pessoa
pessoa1 = Pessoa (nome = input("Digite seu nome aqui:"), idade = int( input ("Digite sua idade aqui: ")))

# Chamar o método para exibir informações
pessoa1.exibir_detalhes()
