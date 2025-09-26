def descrever_cidade(cidade, pais="Brasil"):
    return f'{cidade} esta em {pais}.'


print(descrever_cidade('Maceio'))
print(descrever_cidade('Pequim', 'China'))
print(descrever_cidade('Novo Mexico', 'EUA'))