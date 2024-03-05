import psycopg 
print (psycopg)

class Usuario: 
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

def existe(usuario):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20241_fatec_ipi_pbdi_login_python",
        user="postgres",
        password="123456"
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
                (usuario.login,usuario.senha)
            )
            result = cursor.fetchone()
            #return True if result != None else False
            return result !=None

def teste():
    print(existe(Usuario('admin', 'admin')))

teste()