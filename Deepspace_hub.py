def chatbot_love_deepspace():
    print("--- Bem-vindo ao Deepspace Hub ---")
    print("Olá! Eu sou o assistente interativo da Linkon City.")
    
    # Primeira pergunta
    print("\nVocê conhece o jogo Love and Deepspace?")
    print("1 - Sim, eu jogo!")
    print("2 - Não, nunca ouvi falar.")
    
    resposta_conhece = input("Escolha uma opção (1 ou 2): ")

    if resposta_conhece == "1":
        # Caminho para quem já conhece
        print("\nQue incrível! É sempre bom encontrar outro Deepspace Hunter.")
        print("Dentre esses, qual é o seu personagem favorito?")
        print("1 - Xavier (Lumiere)")
        print("2 - Zayne (Médico Cardíaco)")
        print("3 - Rafayel (O Artista)")
        print("4 - Sylus (O lider da Onychinus)")
        print("5 - Caleb (O Comandante)")
        
        favorito = input("Digite o número do seu favorito: ")
        
        if favorito == "1":
            print("\nXavier... O Caçador das Sombras. Cuidado para não acordá-lo de seus cochilos!")
        elif favorito == "2":
            print("\nZayne. Um pouco frio por fora, mas com um coração de gelo que só você pode derreter.")
        elif favorito == "3":
            print("\nRafayel! Prepare-se para muitas histórias dramáticas e visitas ao estúdio de arte.")
        elif favorito == "4":
            print("\nSylus... Uma escolha intensa. Ele certamente controla a N109 zone.")
        elif favorito =="5":
            print("\nCaleb. Nosso comondante favorito!")
        else:
            print("\nOpção inválida. Mas todos eles são cativantes de sua própria maneira!")

    elif resposta_conhece == "2":
        # (Introdução ao universo)
        print("\nSem problemas! Deixe-me te apresentar:")
        print("Love and Deepspace é um jogo de romance e ficção científica semi-realista.")
        print("Você atua como uma 'Deepspace Hunter', lutando contra criaturas chamadas 'Wanderers'.")
        print("O jogo se passa em 2034, onde humanos possuem habilidades especiais chamadas 'Evol'.")
        print("É uma mistura de combates em 3D com uma história profunda e imersiva.")

        saber_mais = input("Gostaria de saber mais desse mundo?\n 1 - Sim, conte-me mais!\n 2 - Não, obrigado.\nEscolha uma opção (1 ou 2): ")
        if saber_mais == "1":
            print("\nÓtimo! O universo de Deepspace é cheio de mistérios intrigantes.")
            print("Wanderes são monstros cosmicos que carregam um nucleo de energia cosmica\n Algumas pessoas podem acabar sendo transformadas.")
            print("Evol é o poder que uma parte pequena da populaçao tem, \ne pode ser usado para combater os Wanderers ou para outras habilidades especiais.")
    else:
        print("\nOpção inválida. Por favor, reinicie o programa.")

    print("\n--- Obrigado por interagir com o Deepspace Hub! ---")

# Executa o chatbot
chatbot_love_deepspace()