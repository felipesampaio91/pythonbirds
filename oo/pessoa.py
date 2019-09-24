class Pessoa:# Cria a classe pessoa
    olhos = 2 # Atributo de classe

    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade # Atributo idade
        self.nome = nome # Atributo nome
        self.filhos = list(filhos) # Atributo filhos

    def cumprimentar(self):# Método cumprimentar
        return f'Olá {id(self)}'

    @staticmethod #Decorator
    def metodo_estatico(): #Metodo de classe
        return 50
    @classmethod #Decorator
    def nomes_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    antonio = Pessoa(felipe, nome='Antonio')
    print(Pessoa.cumprimentar(antonio))
    print(id(antonio))
    print(antonio.cumprimentar())
    print(antonio.nome)
    print(antonio.idade)
    for filho in antonio.filhos:# atributo dinâmico
        print(filho.nome)
    antonio.sobrenome = 'Oliveira'
    del antonio.filhos # Remoção do atributo dinâmico
    print(antonio.__dict__)# Mostra os atributos de instância do objeto
    print(felipe.__dict__)# Mostra os atributos de instância do objeto
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(antonio.olhos)
    print(felipe.olhos)
    print(id(Pessoa.olhos), id(antonio.olhos), id(felipe.olhos) )
    print(Pessoa.metodo_estatico(), felipe.metodo_estatico())
    print(Pessoa.nomes_e_atributos_de_classe(), felipe.nomes_e_atributos_de_classe())

