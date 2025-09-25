pessoa = {'primeiro_nome':'Pedro', 'sobrenome':'Henrique', 'idade':25}
pessoa['cidade'] = 'Maceió'

for dupla in pessoa.items():
    print(f'chave: {dupla[0]}')
    print(f'valor: {dupla[1]}')

del pessoa['idade']
print(pessoa)