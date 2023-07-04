opcao = -1

while opcao != 0: 
    opcao = int(input("[1] Para sacar \n [2] Para depositar \n [3] Para extrato \n [0] Para sair \n :"))
    if opcao == 1 :
        print("Sacando...")
    elif opcao == 2 :
        print("Esperando deposito")
    elif opcao == 3 :
        print("Imprimindo extrato")
    else:
        print("Obrigado por usar nosso sistema, operação concluida")
