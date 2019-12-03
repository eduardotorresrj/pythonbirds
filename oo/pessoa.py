class Pessoa:
    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return  f'Olá {id(self)}'

if __name__ == '__main__':
    maria = Pessoa(nome='Maria')
    adriana = Pessoa(maria, nome='Adriana')
    print(Pessoa.cumprimentar(adriana))
    print(id(adriana))
    print(adriana.cumprimentar())
    print(adriana.nome)
    print(adriana.idade)
    for filho in adriana.filhos:
        print(filho.nome)
    adriana.sobrenome = 'Torres'
    del adriana.filhos
    print(adriana.__dict__)
    print(maria.__dict__)

