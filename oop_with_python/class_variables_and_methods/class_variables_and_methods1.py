class MyClass:

    static = 'lhama'

    def __init__(self, state) -> None:
        self.state = state

    def print_static(self) -> None:
        print(self.static)

    @classmethod
    def change_static(cls) -> None:
        cls.static = 'Programador'


obj1 = MyClass(True)
obj2 = MyClass(False)

obj1.change_static()

obj1.print_static()
obj2.print_static()
