valorPedido = int(input("Qual foi o valor do pedido: "))
i = 0

while i == 0:
  if valorPedido >= 50:
    print("Parabens, você ganhou uma sobremesa gratis!")
    i += 1
  else:
    print("Que pena, você nao ganhou nenhum brinde especial.")
    i += 1

