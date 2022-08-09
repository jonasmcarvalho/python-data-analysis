from mailbox import NotEmptyError


class Pessoa:

    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def run(self) -> None:
        print('Estou correndo...')

    def beber(self, bebida) -> None:
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('Bebendo...')

    def __apresentar_documento(self) -> None:
        print(self.__cpf)


junior = Pessoa('Junior', 30, '33333333333')
junior.beber('cerveja')
junior.beber('guarana')
