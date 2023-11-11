class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu (self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, "Você conseguiu! Bateu a meta, parabéns!")
        else:
            print(self.nome, "Infelizmente você não bateu a meta, boa sorte na próxima.")


vendedor1 = Vendedor("Rafael")
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

vendedor2 = Vendedor("Thais")
vendedor2.vendeu(300)
vendedor2.bateu_meta(600)