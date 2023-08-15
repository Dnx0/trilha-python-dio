valorHamburguer = float(input("Digite o valor unitario do hamburguer: "))
quantidadeHamburguer = int(input("Quantos hamburgueres: "))
valorBebida = float(input("Digite o valor unitario da bebida: "))
quantidadeBebida = int(input("Quantas bebidas: "))
valorPago = float(input("Quanto foi pago: "))
totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebida = valorBebida * quantidadeBebida
totalPedido = totalHamburguer + totalBebida
troco = valorPago - totalPedido

final = f"O preço final do pedido é R$ {totalPedido:.2f}.Seu troco é R$ {troco:.2f}."
print(final)