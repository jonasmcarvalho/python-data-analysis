class Mother:

    def __init__(self, address: str) -> None:
        self.address = address
        self.last_name = 'Silva'

    def eat(self) -> None:
        print("I'm eating")

    def studying(self) -> None:
        print("I'm studying")


class Daughter(Mother):

    def __init__(self, address: str) -> None:
        super().__init__(address=address)

    def to_play(self, toy: str) -> None:
        print("I'm playing {}".format(toy))


class grand_daugther(Daughter):

    def __init__(self, address: str) -> None:
        super().__init__(address=address)


ana = Mother(address='Rua da Maça')
clara = Daughter(address='Rua do Bolo')
clara.to_play('boneca')
print(ana.address)
print(clara.address)
print(ana.last_name)
