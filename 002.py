saldo = float(input("Digite o valor do seu saldo: "))

def sacar(valor:float):

    if saldo >= valor:
        print("Valor sacado com sucesso e seu saudo é de:")
        print(saldo - valor)
    else: 
        print("Não tem saldo disponivel para saque")

sacar(int(input("Digite o valor que quer sacar: ")))
