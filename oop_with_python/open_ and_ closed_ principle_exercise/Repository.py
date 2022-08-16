class Repository:

    def select(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print('Conectei ao banco {}'.format(connection))
        print('Fazendo um SELECT * FROM...')
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print('Conectei ao banco {}'.format(connection))
        print('Fazendo um Isert Values...')
        db_connection.desconectar()
