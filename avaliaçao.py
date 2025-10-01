avaliacoes = []

print(" AVALIAÇÃO")

while True:
    print("\nO que você quer fazer?")
    print("1 - Adicionar avaliação")
    print("2 - Ver avaliações")

    escolha = input("\nDigite 1 ou 2: ")
   
    if escolha == "1":
        produto = input("Nome do produto: ")
        nota = input("Nota (1 a 5): ")
        comentario = input("Comentário: ")
       
        nova_avaliacao = {
            "produto": produto,
            "nota": nota,
            "comentario": comentario
        }
       
        avaliacoes.append(nova_avaliacao)
        print("Avaliação salva! ")
   
    elif escolha == "2":
        print("\n--- TODAS AS AVALIAÇÕES ---")
       
        if len(avaliacoes) == 0:
            print("Nenhuma avaliação ainda")
        else:
            for av in avaliacoes:
                print(f"Produto: {av['produto']}")
                print(f"Nota: {av['nota']}/5")
                print(f"Comentário: {av['comentario']}")
                print("---")
   
   
    else:
        print("Digite apenas 1, 2 ou 3!")
