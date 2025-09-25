comidas_favoritas = ['a','b','c','d','e']
for comida in comidas_favoritas:
    print("Uma das minhas comidas favoritas é " + comida)

comidas_nao_gosto = ('y','z')
#Tuplas não podem ser afetadas, isso ira subir um TypeError
#comidas_nao_gosto[0] = 'outro prato'

podio = comidas_favoritas[:3]
print('Minhas 3 comidas favoritas são ', podio)