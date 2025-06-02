
lista_lanches = ["Bigmac", "Cheddar McMelt", "McChicken"]
acoes = 5  


while acoes != 0:
    print("\n Lista atual de lanches:")
    if lista_lanches:
        for lanche in lista_lanches:
            print(f"- {lanche}")
    else:
        print("Nenhum lanche na lista.")


    acoes = int(input("\nO que você quer fazer? \n [1] - Fazer pedido de lanche \n [2] - Cancelar pedido \n [0] - Sair\n"))


    if acoes == 1:
        pedido = input("Qual lanche você quer pedir? ")
        if pedido in lista_lanches:
            print(f" Seu lanche '{pedido}' já está sendo preparado! Aguarde um instante.")
        else:
            print(f"Desculpe, '{pedido}' não está disponível no momento.")


    elif acoes == 2:
        excluir = input("Qual lanche você quer cancelar? ")
        if excluir in lista_lanches:
            print(f" Pedido de '{excluir}' cancelado com sucesso!")
        else:
            print("Esse lanche não está na lista!")


    elif acoes == 0:
        print(" Pedido encerrado.")
    else:
        print("Opção inválida. Tente novamente.")
