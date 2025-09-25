convidados = ['carla', 'daniel', 'felipe']
convidados.append('joana')
convidados.insert(0,'bruno')
del convidados[2]
convidado_cancelado = convidados.pop()
convidados.sort()

print("O convidado que cancelou foi: " + convidado_cancelado)
print(convidados)