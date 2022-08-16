class MySqlDB:

    def __init__(self) -> None:
        self.__conexao = 'MySql'

    def conectar(self) -> str:
        print('Conectando ao banco MySql...')
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando ao banco MySql..')
