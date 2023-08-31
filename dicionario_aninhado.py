contato ={
    "joao@gmail.com":{"nome":"joao" , "telefone" : 9999999},
    "maria@gmail.com":{"nome":"maria", "telefone" : 888888},
    "pedro@gmail.com":{"nome":"Pedro", "telefone" : 777777} 
}

telefone = contato["maria@gmail.com"]["telefone"]
print(telefone)

#Loop para ler o dicionario
for chave in contato:
    print(chave,contato[chave])