
from time import sleep
import os

def limpar_tela():
    #IDENTIFICA O SISTEMA E LIMPA A TELA
    os.system('cls' if os.name == 'nt' else 'clear')

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

nome = input("Como podemos lhe chamar? \n")
cad = input(f"{nome} você já possui cadastro? [S/N]").upper()

if cad == "N":
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
            print(f"Cliente: {nome}\n")
    nomecpt = input("Nome completo: \n->")
    nasc = int(input("Ano de nascimento: (AAAA)\n->"))
