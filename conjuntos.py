#sets não permitem valores duplicados
numeros = set([1,2,1,3,3,4,5,2,6]) #valido somente 1,2,3,4,5,6

carros = set(('palio','gol','celta','palio'))#valido somente palio,gol,celta

print(numeros)
print(carros)


#Unindo conjuntos com union
conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))


#Adicionar itens a um conjunto
adicionar = {11,22,33}
adicionar.add(24)#24 foi adicionado
print(adicionar)

#Remover um número de um conjunto

remover = {101,102,103}
remover.discard(101)#101 foi eliminado
print(remover)