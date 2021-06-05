class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    edinaldo = Pessoa(nome='Edinaldo')
    renzo = Pessoa(edinaldo, nome='Renzo')
    print(Pessoa.cumprimentar(renzo))
    print(id(renzo))
    print(renzo.cumprimentar())
    print(renzo.nome)
    print(renzo.idade)
    for filho in renzo.filhos:
        print(filho.nome)
    renzo.sobrenome = 'Nucitelli'
    del renzo.filhos
    print(renzo.__dict__)
    print(edinaldo.__dict__)
