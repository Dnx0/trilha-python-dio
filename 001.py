#Função em python
def sacar(valor):
    saldo = 500

    if saldo >= valor:
      print("Valor sacado com sucesso e seu saudo é de:")
      print (saldo - valor)

sacar(55)