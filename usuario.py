class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self.funcao = None

    def salvar_funcao(self, funcao: str):
        self.funcao = funcao

    def __str__(self):
        return f'Usuário: {self.nome}, Função: {self.funcao}'
