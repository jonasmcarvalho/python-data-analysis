class Person:

    def __init__(self, name: str) -> None:
        self.__place = None
        self.__name = name

    def enter_the_place(self) -> None:
        self.__place.turn_on_light()

    def present_location(self) -> None:
        address = self.__place.get_address()
        print(address)

    def introduce_yourself(self) -> None:
        print("Hello, I'm {}".format(self.__name))

    def local_set(self, place: any) -> None:
        self.__place = place

    def local_get(self) -> any:
        return self.__place
