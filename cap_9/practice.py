class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome, idade):
        self.primeiro_nome =  primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        
    def descrever_usuario(self):
        return f'Primeiro nome: {self.primeiro_nome}\nUltimo nome: {self.ultimo_nome}\nIdade: {self.idade}'
    
    def saudar_usuario(self):
        print(f'Olá! Meu nome é {self.primeiro_nome}, prazer.')


class Admin(Usuario):
    def __init__(self, primeiro_nome, ultimo_nome, idade, privilegios):
        super().__init__(primeiro_nome, ultimo_nome, idade)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        return self.privilegios
    

admin = Admin('pedro','oliveira', 25, ['pode adicionar post', 'pode deletar post', 'pode banir usuário'])
print(admin.mostrar_privilegios())