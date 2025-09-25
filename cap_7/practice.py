
running = True 
while running:

    ingrediente = input("Insira o ingrediente: ")
    
    if ingrediente == "sair":
        running = False
    else:
        print(f'{ingrediente} adicionado!')

if ingrediente:
    print('Sua Pizza esta sendo preparada!')
    