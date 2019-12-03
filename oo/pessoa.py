class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return  f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    adriana.olhos = 1
    del adriana.olhos
    print(adriana.__dict__)
    print(maria.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(adriana.olhos)
    print(maria.olhos)
    print(id(Pessoa.olhos), id(adriana.olhos), id(maria.olhos))
    print(Pessoa.metodo_estatico(), adriana.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), adriana.nome_e_atributos_de_classes())

