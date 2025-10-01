class ItemCarrinho:
    def __init__(self, nome, preco, quantidade=1, observacoes="", configuracoes="", fornecedor="", estoque=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.observacoes = observacoes
        self.configuracoes = configuracoes
        self.fornecedor = fornecedor
        self.estoque = estoque
        self.total = preco * quantidade
   
    def mostrar_item(self):
        print(f" {self.nome}")
        print(f"   Preço: R$ {self.preco:.2f}")
        print(f"   Quantidade: {self.quantidade}")
        print(f"   Total: R$ {self.total:.2f}")
        print(f"   Fornecedor: {self.fornecedor}")
        print(f"   Estoque: {self.estoque} unidades")
        if self.observacoes:
            print(f"   Observações: {self.observacoes}")

class Carrinho:
    def __init__(self, id_carrinho):
        self.id_carrinho = id_carrinho
        self.itens = []  
        self.quantidade_item = 0
        self.total = 0.0
        self.desconto = 0.0
   
    def adicionar_item(self, nome, preco, quantidade=1, observacoes="", configuracoes="", fornecedor="", estoque=0):
        novo_item = ItemCarrinho(nome, preco, quantidade, observacoes, configuracoes, fornecedor, estoque)
       
        self.itens.append(novo_item)
       
        self.quantidade_item += quantidade
        self.total += novo_item.total
       
        print(f" '{nome}' adicionado ao carrinho!")
   
    def mostrar_carrinho(self):
        print(f"\n CARRINHO #{self.id_carrinho}")
        print("=" * 40)
       
        if len(self.itens) == 0:
            print("carrinho vazio")
            return
       
        for i, item in enumerate(self.itens, 1):
            print(f"{i}. ", end="")
            item.mostrar_item()
            print("-" * 30)
       
        print(f" TOTAL DO CARRINHO:")
        print(f"   Itens: {self.quantidade_item}")
        print(f"   Valor: R$ {self.total:.2f}")
   
    def remover_item(self, numero_item):
        if 1 <= numero_item <= len(self.itens):
            item_removido = self.itens.pop(numero_item - 1)
           
            self.quantidade_item -= item_removido.quantidade
            self.total -= item_removido.total
           
            print(f"'{item_removido.nome}' removido do carrinho!")
        else:
            print("Item não encontrado!")

def main():
    meu_carrinho = Carrinho(id_carrinho=1)
   
    while True:
        print("\n1. Ver carrinho")
        print("2. Adicionar item")
        print("3. Remover item")
       
        opcao = input("Escolha uma opção: ")
       
        if opcao == "1":
            meu_carrinho.mostrar_carrinho()
       
        elif opcao == "2":
            print("\nADICIONAR ITEM")
            nome = input("Nome do produto: ")
            preco = float(input("Preço: R$ "))
            quantidade = int(input("Quantidade: ") or "1")
            fornecedor = input("Fornecedor: ")
            estoque = int(input("Estoque disponível: "))
            observacoes = input("Observações (opcional): ")
            configuracoes = input("Configurações (opcional): ")
           
            meu_carrinho.adicionar_item(nome, preco, quantidade, observacoes, configuracoes, fornecedor, estoque)
       
        elif opcao == "3":
            meu_carrinho.mostrar_carrinho()
            if meu_carrinho.itens:
                numero = int(input("Número do item a remover: "))
                meu_carrinho.remover_item(numero)

print("LOJA")
main()
