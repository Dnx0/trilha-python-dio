#Função em pyton antecessor e sucessor

numero = int(input("Digite um número para obter o seu antecessor e sucessor: "))

def antecessor_sucessor (numero):
    antecessor = numero -1
    sucessor = numero + 1
    return antecessor,sucessor

#função somar todos elementos de uma tupla
tupla = (1,2,3,4,5)
def somar_todos(tupla):
    return sum(tupla)

print(antecessor_sucessor(numero))
print(somar_todos(tupla))