"# Jogo_forca.py" 

# Projeto 1  - desenvimento de um game em Python - versão 1 

# import
import random
from os import system, name

# Função limpar tela a cada execução 
def limpar_tela():

    # Windows 
    if name == 'nt':
        _= system('cls')

    # Mac ou linux 
    else:
        _= system('clear')

# Função 
def game():

    limpar_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe qual fruta é:\n")

    # Lista de frutas 
    palavra = ['abacate', 'abacaxi', 'banana', 'maça', 'mamao', 'manga', 'melao', 'pera', 'tomate', 'uva', 'laranja ', 'morango ' ]
    
    # Escolha randomicamente uma palavra 
    palavra = random.choice(palavra)

    # List comprehension 
    letras_descobertas = ['_' for letra in palavra]

    # Número de chance 
    chances = 7 

    # Lista para letras erradas
    letras_erradas = []

    # Loop enquanto número  de chance for maior que zero 
    while chances > 0:

        # Print 
        print("".join(letras_descobertas))
        print("\nChances restante:", chances)
        print("Letras tras erradas:"," ".join(letras_erradas))

        # Tentativa 
        tentativa = input("\nDigite uma letra:").lower()

        # Condicional
        if tentativa in palavra:
            index = 0 
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra 
                index += 1 
        else:
            chances -=1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            print("Voçê Venceu, a palavra era:", palavra)
            break

    # Condicional 
    if "_" in letras_descobertas:
        print("Voçê perdeu, a palavra era:", palavra)

# Bloco man 
if __name__=="__main__":
    game()
    print("\nParabéns para min meu primeiro projeto em Python!")
