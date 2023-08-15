#Inicio do While
opcao = -1

#Variaveis do Saque, máximo do saque 500 por saque e até 3x por dia
limiteSaque = 500
saqueDia = 3
valorSacado = 0

#Variaveis do Saldo
saldo = float(0)

#Variaveis Deposito
deposito = float(0)
while opcao != 0: 
    opcao = int(input(" [1] Para sacar \n [2] Para depositar \n [3] Para extrato \n [0] Para sair \n :"))
    #Opção de Saque
    if opcao == 1 :
      saque = float(input("Digite o valor a ser sacado: "))                     
      if saldo <= 0 :
        print ("Conta zerado, não é possivel realizar o saque")
        continue
      if saldo < saque:
         print("Não há fundos suficientes para realizar o saque!!!") 
         continue
      if saque > 500:
         print ("Valor indisponivel para saque, somente saques abaixo de 500")
         continue
      if saque <= 0:
         print("Erro, valor impossivel de sacar")
      if   saqueDia <= 0:
         print("Sem saques diarios restantes") 
         continue
      else:
         saqueDia -= 1
         saldo -= saque
         print("Valor sacado com sucesso.")
    #Opção de Deposito
    elif opcao == 2 :
        deposito = float(input("Digite o valor do deposito: "))
        if deposito > 0:
           saldo += deposito
           print("Deposito realizado com sucesso.")
        else:
           print("Deposito falhou, valor invalido!!!")
    #Opção de Extrato       
    elif opcao == 3 :
        print("Imprimindo extrato, só um momento:")        
        print(saldo)
    else:
        print("Obrigado por usar nosso sistema, operação concluida")
