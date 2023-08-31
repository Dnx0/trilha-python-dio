valorPedido = float(input("Qual foi o valor do pedido: "))
i = 0
sobremesa = 50

while i == 0:
  if valorPedido >= sobremesa:
    print("Parabens, você ganhou uma sobremesa gratis!")
    i += 1
  else:
    print("Que pena, você nao ganhou nenhum brinde especial.")
    print(f"Faltou { sobremesa - valorPedido } reais para ganhar o brinde")
    i += 1

  