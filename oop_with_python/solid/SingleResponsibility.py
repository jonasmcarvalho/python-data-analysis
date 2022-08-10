class CadastralSystem:

    def register(self, name: str, age: int):
        if self.__check_data(name, age):
            self.__store_user(name, age)
        else:
            self.__indicate_error()

    def __check_data(self, name: str, age: int) -> bool:
        if isinstance(name, str) and isinstance(age, int):
            return True
        else:
            return False

    def __store_user(self, name: str, age: int) -> None:
        print('Accessing the database')
        print('Register the user {}, age {}'.format(name, age))

    def __indicate_error(self) -> None:
        print('Invalid data')


cadastral_data = CadastralSystem()

cadastral_data.register('Jonas', 33)
cadastral_data.register('Jonas', '33')
cadastral_data.register(123, 'Jonas')
