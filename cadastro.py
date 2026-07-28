
from time import sleep
import os
import sqlite3
import cardapio

def limpar_tela():
    #IDENTIFICA O SISTEMA E LIMPA A TELA
    os.system('cls' if os.name == 'nt' else 'clear')

def conectar_banco():

    conexao = sqlite3.connect("loja.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    conexao.commit()
    return conexao

def cadastrar_usuario(cpf, nome, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (cpf, nome, senha) VALUES (?, ?, ?)",
            (cpf, nome, senha)
        )
        conexao.commit()
        print("\n✅ Cadastro Realizado com Sucesso!")
        return True
    except sqlite3.IntegrityError:
        print("\n❌ ERRO: Esse CPF já está cadastrado no sistema!")
        return False
    finally:
        conexao.close()

def fazer_login(cpf, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    #Busca o usuario pelo CPF
    cursor.execute(
        "SELECT nome FROM usuarios WHERE cpf = ? AND senha = ?",
        (cpf, senha)
    )
    usuario = cursor.fetchone()
    conexao.close()

    if usuario:
        print(f"\n Login Realizado com Sucesso!")
        sleep(1)
        print(f"Seja bem vindo(a), {usuario[0]}!")
        return True
    else:
        print(f"CPF ou Senha Incorretos!")
        return False

def validar_cpf(cpf: str) -> bool:
    #LIMPA O CPF E MANTEM SO NUMEROS
    cpf_limpo = "".join(filter(str.isdigit, cpf))

    #VERIFICA SE TEM EXATAMENTE 11 DIGITOS
    if len(cpf_limpo) != 11:
        return False

    #ELIMINA CPFs COM TODOS OS NUMEROS IGUAIS
    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    #CALCULA O PRIMEIRO DIGITO VERIFICADOR
    soma = 0
    #MULTIPLICA OS 9 PRIMEIROS DIGITOS POR PESOS DE 10 A 2
    for i, peso in enumerate(range(10, 1, -1)):
        soma += int(cpf_limpo[i]) * peso

    resto = (soma * 10) % 11
    primeiro_digito = 0 if resto == 10 or resto == 11 else resto

    #SE O PRIMEIRO DIGITO CALCULADO FOR DIFERENTE DO 10 DIGITO DO CPF, É INVALIDO
    if primeiro_digito != int(cpf_limpo[9]):
        return False

    #CALCULA O SEGUNDO DIGITO VERIFICADOR 
    soma = 0
    #MULTIPLICA OS 10 PRIMEIROS DIGITOS POR PESOS DE 11 A 2
    for i, peso in enumerate(range(11, 1, -1)):
        soma += int(cpf_limpo[i]) * peso

    resto = (soma * 10) % 11
    segundo_digito = 0 if resto == 10 or resto == 11 else resto

    #SE O SEGUNDO DIGITO CALCULADO FOR DIFERENTE DO 11 DIGITO DO CPF É INVALIDO
    if segundo_digito != int(cpf_limpo[10]):
        return False

    #SE PASSAR POR TODAS AS VERIFICAÇÕES, O CPF É VÁLIDO!
    return True

print("=== Seja bem vindo(a) a Doceria Express! ===")
print("Antes de continuar, Precisamos confirmar algumas informações...")

apelido = input("Como podemos lhe chamar? \n")
opcao = input(f"{apelido} você já possui cadastro? [S/N] \n-> ").upper()

if opcao == "N":
    print("Sem problemas! \nVamos realizar o seu cadastro rapidinho!")
    sleep(1)
    print("Só precisamos de algumas informações...")
    while True:
        cpf = input("CPF: (APENAS NÚMEROS) \n->")
        if validar_cpf(cpf):
            print('CPF válido!')
            break
        else:
            print("CPF Inválido! Verifique os Dígitos digitados.")
            sleep(1.5)
            limpar_tela()
            print("=== CADASTRO - DOCERIA EXPRESS ===")
            print(f"Cliente: {apelido}\n")
    if validar_cpf(cpf):
        nome = input("Digite seu nome: ")
        senha = input("Crie uma senha: ")
        #Salvar no bando de dados SQLite
        cadastrar_usuario(cpf, nome, senha)
    print("Cadastro realizado com sucesso!")
    sleep(1)
    print("Agora vamos agora realizar o seu login!")
    sleep(3)
    limpar_tela()
    while True:
        cpf = input("Digite seu CPF: (APENAS NÚMEROS) \n->")
        sleep(0.5)
        senha = input("Digite sua senha: \n->")
        sleep(0.5)

        if fazer_login(cpf, senha):
            print("Carregando Cardápio...")
            sleep(1.5)
            limpar_tela()

            cardapio.exibir_cardapio_completo()

        else:
            print("Usuário e/ou Senha incorretos! Tente novamente.")
            sleep(1)
            limpar_tela()
            break
