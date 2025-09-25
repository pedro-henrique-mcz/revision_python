nome_famoso = "albert einstein"
citacao = "Uma pessoa que nunca cometeu um erro jamais tentou nada novo."
ano_nascimento = 1879

message = nome_famoso.title()
message += " (nascido em " + str(ano_nascimento) + ") uma vez disse:"
message += '"'+ citacao + '"'

print(message)