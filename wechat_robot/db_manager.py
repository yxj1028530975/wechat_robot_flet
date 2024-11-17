import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self.create_database_if_not_exists()

    def create_database_if_not_exists(self):
        if not os.path.exists(self.db_path):
            # Crie o banco de dados ou realize outras operações necessárias
            with sqlite3.connect(self.db_path) as con:
                self.create_tables()

    def create_tables(self):
        # Adicione aqui a lógica para criar todas as tabelas necessárias
        self.execute('''
            CREATE TABLE IF NOT EXISTS user(
                nome TEXT,
                sobrenome TEXT,
                email TEXT,
                telefone TEXT,
                password TEXT
            )
        ''')
        # Adicione outras tabelas conforme necessário


    def execute(self, query, params=None):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            con.commit()
            return cur.fetchall()