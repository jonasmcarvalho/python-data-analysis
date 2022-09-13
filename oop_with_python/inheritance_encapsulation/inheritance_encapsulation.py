class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'Lhama'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self) -> None:
        print('Connection OK!')


class Repository(DatabaseConn):

    def __init__(self) -> None:
        super().__init__()
        print(self.user)
        # print(self.__database) #error
        print(self._conn)

    def select(self) -> None:
        self._testing_connection()
        print('connectiong to {}'.format(self._conn))
        print('SELECT * FROM table')


db = DatabaseConn()

print(db.user)
# print(db.__database)  # error
print(db._conn)  # it was supposed to give an error but in python it doesn't
db._testing_connection()

repo = Repository()

repo.select()
