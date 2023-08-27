#argumento nomedo chave e valor
def salvar_carro(marca,modelo,ano,placa):
    print(f"Carro atualizado com sucesso {marca}/{modelo}/{ano}/{placa}")

#chave e valor
salvar_carro(marca="Fiat",modelo="uno",ano="1999",placa="cua0800")

#Dicionario
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 2001, "placa": "fal6915"})
#** despacotamento de dicionario kwargs