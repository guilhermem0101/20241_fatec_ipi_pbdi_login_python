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


def inserir(usuario):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20241_fatec_ipi_pbdi_login_python",
        user="postgres",
        password="123456"
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_usuario(login, senha)  VALUES(%s, %s) RETURNING login',
                (usuario.login,usuario.senha)
            )
            result = cursor.fetchone()
            #return True if result != None else False
            return result !=None


def menu():
    texto = '0-Sair\n1-Login\n2-Logoff\n3-Criar usuario'
    usuario = None
    op = int(input(texto))
    while op !=0:
        if op == 1:
            login = input('Digite o login ')
            senha = input('Digite o senha ')
            usuario = Usuario(login, senha)
            print('Usuario OK!' if existe(usuario) else 'Usuario NOK')
        elif op == 2:
            usuario = None
            print('Logoff realizado com sucesso')
        elif op == 3:
            login = input('Digite o login ')
            senha = input('Digite o senha ')
            usuario = Usuario(login, senha)
            inserir(usuario)
            #print('Usuario Criado!' if inserir(usuario) else 'Usuario Não criado')
        else:
            print('digite a opção válida')
        op == int(input(texto))

menu()
# def teste():
#     print(existe(Usuario('admin', 'admin')))

# teste()

