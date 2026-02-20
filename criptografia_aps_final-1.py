import random  # Importa a biblioteca random para gerar números aleatórios
import os  # Importa a biblioteca os para executar comandos no sistema operacional

# Função para limpar a tela
def limpar_tela():
    # Limpa a tela
    os.system('cls')

# Função para a cifra de Vigenère que ignora espaços na chave
def cifra_vigenere(texto, chave, criptografar=True):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Define o alfabeto para facilitar o cálculo do índice das letras
    resultado = []  # Cria uma lista para armazenar o resultado da criptografia ou descriptografia
    chave = chave.replace(" ", "").upper()  # Remove espaços da chave e converte para maiúsculas
    tam_chave = len(chave)  # Calcula o comprimento da chave para fazer o ciclo dela no texto
    indice_chave = 0  # Variável para controlar a posição atual na chave

    # Itera sobre cada caractere do texto
    for caractere in texto.upper():  # Converte o texto para maiúsculas e percorre caractere por caractere
        if caractere in alfabeto:  # Verifica se o caractere atual está no alfabeto (ignora caracteres especiais)
            caractere_chave = chave[indice_chave % tam_chave]  # Seleciona o caractere da chave usando o índice atual
            deslocamento = alfabeto.index(caractere_chave)  # Calcula o deslocamento baseado no índice da letra da chave
            indice_caractere = alfabeto.index(caractere)  # Encontra o índice do caractere atual do texto
            if criptografar:  # Se está no modo de criptografia
                resultado.append(alfabeto[(indice_caractere + deslocamento) % 26])  # Adiciona a letra cifrada ao resultado
            else:  # Se está no modo de descriptografia
                resultado.append(alfabeto[(indice_caractere - deslocamento) % 26])  # Adiciona a letra decifrada ao resultado
            indice_chave += 1  # Avança a posição na chave se o caractere estiver no alfabeto
        else:
            resultado.append(caractere)  # Mantém caracteres que não estão no alfabeto, como espaços e pontuação

    return ''.join(resultado)  # Concatena todos os caracteres na lista 'resultado' em uma string final

# Função para a cifra de César
def cifra_cesar(texto, deslocamento, criptografar=True):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Define o alfabeto para uso na cifra de César
    resultado = []  # Cria uma lista para armazenar o resultado
    deslocamento = deslocamento if criptografar else -deslocamento  # Define o deslocamento como negativo para descriptografar

    # Itera sobre cada caractere do texto
    for caractere in texto.upper():  # Converte o texto para maiúsculas e percorre caractere por caractere
        if caractere in alfabeto:  # Verifica se o caractere está no alfabeto
            indice_caractere = alfabeto.index(caractere)  # Encontra o índice do caractere atual no alfabeto
            resultado.append(alfabeto[(indice_caractere + deslocamento) % 26])  # Adiciona o caractere cifrado ao resultado
        else:
            resultado.append(caractere)  # Mantém caracteres que não estão no alfabeto

    return ''.join(resultado)  # Concatena todos os caracteres na lista 'resultado' em uma string final

# Função principal que controla o fluxo do programa
def principal():
    print("Bem-vindo ao software de criptografia!\n")  # Mensagem inicial
    print("Instruções: escolha a ação desejada\ne insira o texto para criptografar/descriptografar.")

    while True:
        # Exibe o menu principal
        print("\nEscolha uma ação:")
        print("\n1. Criptografar o texto")
        print("2. Descriptografar o texto")
        print("3. Limpar a tela")
        print("4. Sair do programa")
        escolha = input("\nDigite a opção desejada (1, 2, 3 ou 4): ").strip()  # Recebe a escolha do usuário

        # Criptografia
        if escolha == '1':
            texto = input("\nDigite o texto para criptografar (máximo 128 caracteres): ").strip()  # Solicita o texto
            if len(texto) > 128:  # Verifica se o texto excede 128 caracteres
                print("\nErro: o texto excede 128 caracteres. Tente novamente.")
                continue  # Retorna ao menu principal

            chave = input("\nDigite a chave de Vigenère\n(apenas letras): ").strip()  # Solicita a chave de criptografia
            if not chave.replace(" ", "").isalpha():  # Verifica se a chave contém apenas letras e espaços
                print("\nErro: a chave deve conter apenas letras e espaços. Tente novamente.")
                continue  # Retorna ao menu principal

            texto_criptografado = cifra_vigenere(texto, chave, criptografar=True)  # Aplica a cifra de Vigenère
            print("\nTexto criptografado (1ª camada - Vigenère):", texto_criptografado)  # Exibe o texto cifrado

            # Pergunta sobre a segunda camada de criptografia com César
            print("\nDeseja adicionar uma segunda camada de criptografia com a Cifra de César?")
            print("\n1. Sim")
            print("2. Não")
            escolha_segunda_camada = input("Escolha: ").strip()  # Recebe a escolha do usuário

            if escolha_segunda_camada == '1':
                deslocamento_cesar = random.randint(1, 1000)  # Gera um número aleatório entre 1 e 1000 para o deslocamento
                texto_criptografado = cifra_cesar(texto_criptografado, deslocamento_cesar, criptografar=True)  # Aplica César
                print("\nTexto criptografado (2ª camada - César):", texto_criptografado)  # Exibe o texto cifrado
                print("Chave de César para descriptografar (2ª camada):", deslocamento_cesar)  # Exibe a chave para descriptografar

        # Descriptografia
        elif escolha == '2':
            texto = input("\nDigite o texto para descriptografar (máximo 128 caracteres): ").strip()  # Solicita o texto cifrado
            if len(texto) > 128:  # Verifica se o texto excede 128 caracteres
                print("\nErro: o texto excede 128 caracteres. Tente novamente.")
                continue  # Retorna ao menu principal

            # Pergunta sobre o tipo de descriptografia
            print("\nEscolha o tipo de descriptografia:")
            print("\n1. Descriptografar somente a 1ª camada (Vigenère)")
            print("2. Descriptografar ambas as camadas (Vigenère e César)")
            camadas = input("\nEscolha: ").strip()  # Recebe a escolha do usuário para as camadas de descriptografia

            if camadas == '1':  # Descriptografa apenas a primeira camada (Vigenère)
                chave = input("\nDigite a chave de Vigenère usada para criptografia\n(apenas letras): ").strip()  # Solicita a chave de Vigenère
                if not chave.replace(" ", "").isalpha():  # Valida a chave para conter apenas letras e espaços
                    print("\nErro: a chave deve conter apenas letras e espaços. Tente novamente.")
                    continue  # Retorna ao menu principal
                texto_desencriptado = cifra_vigenere(texto, chave, criptografar=False)  # Descriptografa o texto usando Vigenère
                print("\nTexto desencriptado:", texto_desencriptado)  # Exibe o texto descriptografado

            elif camadas == '2':  # Descriptografa ambas as camadas (Vigenère e César)
                chave = input("\nDigite a chave de Vigenère usada para criptografia\n(apenas letras): ").strip()  # Solicita a chave de Vigenère
                if not chave.replace(" ", "").isalpha():  # Valida a chave para conter apenas letras e espaços
                    print("\nErro: a chave deve conter apenas letras e espaços. Tente novamente.")
                    continue  # Retorna ao menu principal
                deslocamento_cesar = int(input("Digite a chave de César usada (2ª camada): ").strip())  # Solicita a chave de César
                texto_primeira_camada = cifra_cesar(texto, deslocamento_cesar, criptografar=False)  # Descriptografa a segunda camada (César)
                texto_desencriptado = cifra_vigenere(texto_primeira_camada, chave, criptografar=False)  # Descriptografa a primeira camada (Vigenère)
                print("\nTexto desencriptado (ambas as camadas):", texto_desencriptado)  # Exibe o texto descriptografado (ambas as camadas)

            else:
                print("\nOpção inválida. Por favor, selecione 1 ou 2.")  # Exibe uma mensagem para opção inválida de camada

        # Limpar a tela
        elif escolha == '3':
            limpar_tela()  # Chama a função para limpar a tela

        # Sair
        elif escolha == '4':
            print("\nEncerrando o programa. Até logo!")  # Mensagem de despedida
            break  # Encerra o loop e o programa

        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")  # Mensagem de erro para uma escolha inválida no menu

# Executa a função principal
principal()  # Inicia o programa
