class Pessoa:
    def __init__(self, nome=None, idade=34):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return  f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Adriana')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Carlos'
    print(p.nome)
    print(p.idade)