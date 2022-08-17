from typing import Type

class House:
    def __init__(self) -> None:
        self.__address = 'Rua dos Limoeiros'

    def turn_on_light(self) -> None:
        print("I'm turning on the lights")

    def get_address(self) -> str:
        return self.__address


class Person:
    def __init__(self, name: str, local: Type[House]) -> None:
        self.__local = local
        self.__name = name

    def enter_the_place(self) -> None:
        self.__local.turn_on_light()

    def present_location(self) -> None:
        address = self.__local.get_address()
        print(address)

friend_house = House()
ana = Person('Ana', friend_house)

ana.enter_the_place()
ana.present_location()

