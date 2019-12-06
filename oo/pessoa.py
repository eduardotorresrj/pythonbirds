class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return  f'Olá, meu nome é  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    eduardo = Homem(nome='Eduardo')
    carlos = Mutante(eduardo, nome='Carlos')
    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(filho.nome)
    carlos.sobrenome = 'Torres'
    del carlos.filhos
    carlos.olhos = 1
    del carlos.olhos
    print(carlos.__dict__)
    print(eduardo.__dict__)
    print(Pessoa.olhos)
    print(carlos.olhos)
    print(eduardo.olhos)
    print(id(Pessoa.olhos), id(carlos.olhos), id(eduardo.olhos))
    print(Pessoa.metodo_estatico(), carlos.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), carlos.nome_e_atributos_de_classes())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(carlos, Pessoa))
    print(isinstance(carlos, Homem))
    print(carlos.olhos)
    print(eduardo.cumprimentar())
    print(carlos.cumprimentar())
