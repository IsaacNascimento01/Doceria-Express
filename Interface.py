from time import sleep

def escolha_sabores():
    # Dicionário com os sabores mapeados pelo número
    cardapio = {
        "1": "Tradicional de Chocolate",
        "2": "Tradicional de Ninho",
        "3": "Tradicional de Prestígio",
        "4": "Gourmet de Crocante de Amendoim",
        "5": "Gourmet de Mesclado",
        "6": "Gourmet de Café",
        "7": "Gourmet de Nesquik",
        "8": "Frutado de Maracujá",
        "9": "Frutado de Limão"
    }

    # Mostra o menu de opções na tela
    print("\n=== CARDÁPIO DE SABORES ===")
    print("[ 1 ] Tradicional de Chocolate \n[ 2 ] Tradicional de Ninho \n[ 3 ] Tradicional de Prestígio")
    print("[ 4 ] Gourmet de Crocante de Amendoim \n[ 5 ] Gourmet de Mesclado \n[ 6 ] Gourmet de Café \n[ 7 ] Gourmet de Nesquik")
    print("[ 8 ] Frutado de Maracujá \n[ 9 ] Frutado de Limão")
    print("=" * 27)

    sabores_escolhidos = []

    print("\nVocê pode escolher até 4 sabores!")

    # O for roda exatamente 4 vezes (de 1 até 4)
    for i in range(1, 5):
        while True:
            opcao = input(f"Escolha o {i}º sabor (digite o número): ")

            # Verifica se o número digitado existe no cardápio
            if opcao in cardapio:
                sabor_nome = cardapio[opcao]
                sabores_escolhidos.append(sabor_nome)
                print(f"✅ {sabor_nome} adicionado!")
                break # Sai do 'while' e vai para a próxima repetição do 'for'
            else:
                print("❌ Opção inválida! Escolha um número de 1 a 9.")

    return sabores_escolhidos


cardapio = {
    "🍫 TRADICIONAIS": ["Chocolate", "Ninho", "Prestígio"],
    "✨ GOURMET": ["Amendoim", "Crocante", "Mesclado", "Café", "Nesquik"], # Adicionada a vírgula aqui
    "🍓 FRUTADOS": ["Maracujá", "Limão"]
}

print("=== MENU F & I DOCERIA EXPRESS ===")
print("\nDigite o número da opção desejada")

print("\n[ 1 ] Cardápio de MOUSSES \n[ 2 ] Cardápio de brigadeiros \n[ 3 ] Sair")
resposta = int(input("-> "))

if resposta == 1:
    print("=== CARDÁPIO DE MOUSSES ===")
    print("\nDigite a opção desejada:")

    print("\n[ 1 ] Mousse de Chocolate \n[ 2 ] Mousse de Limão \n[ 3 ] Mousse de Morango \n[ 4 ] Mousse de Maracujá \n[ 5 ] Mousse de Paçoca")
    resposta = int(input("-> "))

elif resposta == 2:
    print("=== CARDÁPIO DE BRIGADEIROS ===")
    print("\nDigite a opção desejada:")

    print("\n[ 1 ] CAIXINHAS DA FELICIDADE \n[ 2 ] ENCOMENDA PROGRAMADA")
    resposta = int(input("-> "))

    if resposta == 1:
        print("\nNossas Caixinhas da felicidade contêm 4 unidades, podendo escolher até 4 sabores.")
        sleep(1.5)
        print("Os sabores que temos são:")
        
        for categoria, lista_doces in cardapio.items():
            print(f"\n=== {categoria} ===")
            for doce in lista_doces:
                print(f"  • {doce}")
                
        sleep(2)
        escolha = input("\nPodemos prosseguir? [ S / N ]\n-> ").upper().strip()
        
        if escolha == "S":
            # Chamando a função
            meus_sabores = escolha_sabores()

            # Exibindo o resultado final
            print("\n=== RESUMO DAS SUAS 4 ESCOLHAS ===")
            for sabor in meus_sabores:
                print(f"• {sabor}")
        else:
            print("\nEntendido! Retornando ao menu principal...")
