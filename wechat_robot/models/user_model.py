import sqlite3

class UserModel:
    # Example user model
    def __init__(self, dados_usuario, db_manager):
        self.db_manager = db_manager
        self.nome =  dados_usuario['nome']
        self.sobrenome = dados_usuario['sobrenome']
        self.email = dados_usuario['email']
        self.telefone = dados_usuario['telefone']
        self.password = dados_usuario['password']
    

    # Add methods for user authentication, data retrieval, etc.
        
    def add_userdb(self):
        self.db_manager.execute(query='INSERT INTO user VALUES(?,?,?,?,?)', params=[self.nome, self.sobrenome, self.email, self.telefone,
                                                                            self.password])

    def select_userdb(self):
        pass

    def delete_userdb(self):
        pass