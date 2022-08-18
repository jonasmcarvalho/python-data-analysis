class House:

    def __init__(self) -> None:
        self.__address = 'Rua dos Limoeiros'
        self.__owner = None

    def turn_on_light(self) -> None:
        print("I'm turning the lights on")

    def get_address(self) -> None:
        return self.__address

    def set_owner(self, owner: any) -> None:
        self.__owner = owner

    def get_owner(self) -> any:
        return self.__owner
