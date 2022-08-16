from Repository import Repository
from databases import PostgresDB, MySqlDB

db_connection_postgress = PostgresDB()
db_connection_mysql = MySqlDB()
repository = Repository()

repository.insert(db_connection=db_connection_postgress)
print()
repository.insert(db_connection=db_connection_mysql)
