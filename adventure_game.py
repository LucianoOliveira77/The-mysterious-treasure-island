import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def get_valid_input(options):
    while True:
        choice = input("\nSua escolha (digite o número): ").strip()
        if choice in options:
            return choice
        print("Opção inválida! Por favor, escolha um número válido.")

def introduction():
    clear_screen()
    print_slow("""
    ╔══════════════════════════════════════════════╗
    ║         A ILHA DO TESOURO MISTERIOSO         ║
    ╚══════════════════════════════════════════════╝
    """)
    print_slow("\nVocê é um explorador destemido em busca do lendário tesouro perdido.")
    print_slow("Após anos de pesquisa, você finalmente chegou à misteriosa Ilha das Sombras.")
    print_slow("Dizem que o tesouro está escondido em algum lugar desta ilha...")
    print_slow("\nPressione ENTER para começar sua aventura...")
    input()

def play_game():
    health = 100
    has_map = False
    has_torch = False
    
    while True:
        clear_screen()
        print(f"\nSaúde atual: {health}%")
        
        # Primeira escolha - Ponto inicial
        print_slow("\nVocê está na praia da ilha. À sua frente existem três caminhos:")
        print("\n1. Entrar na densa selva")
        print("2. Explorar a praia em busca de suprimentos")
        print("3. Escalar o penhasco próximo")
        
        choice = get_valid_input(['1', '2', '3'])
        
        if choice == '1':  # Selva
            print_slow("\nVocê adentra a densa selva...")
            print_slow("Você encontra uma bifurcação:")
            print("\n1. Seguir o caminho com pegadas")
            print("2. Seguir o caminho com marcas nas árvores")
            
            path_choice = get_valid_input(['1', '2'])
            
            if path_choice == '1':
                print_slow("\nVocê segue as pegadas e encontra um tigre!")
                print("\n1. Tentar fugir")
                print("2. Subir em uma árvore")
                
                tiger_choice = get_valid_input(['1', '2'])
                
                if tiger_choice == '1':
                    print_slow("\nVocê tenta fugir, mas o tigre é mais rápido!")
                    health -= 50
                    if health <= 0:
                        return "Você não sobreviveu ao encontro com o tigre..."
                    print_slow(f"Você conseguiu escapar, mas ficou ferido. Saúde: {health}%")
                else:
                    print_slow("\nVocê sobe na árvore a tempo e o tigre vai embora.")
                    print_slow("Você encontra um mapa antigo no galho da árvore!")
                    has_map = True
            
            else:
                print_slow("\nAs marcas nas árvores levam a uma pequena cabana abandonada.")
                print_slow("Você encontra uma tocha e fósforos!")
                has_torch = True
                
        elif choice == '2':  # Praia
            if not has_map:
                print_slow("\nProcurando na praia, você encontra uma garrafa com uma mensagem!")
                print_slow("É um pedaço de um mapa do tesouro!")
                has_map = True
            else:
                print_slow("\nVocê não encontra mais nada útil na praia...")
                
        else:  # Penhasco
            if has_map and has_torch:
                print_slow("\nDo alto do penhasco, você avista uma caverna!")
                print_slow("Com o mapa e a tocha, você pode explorar com segurança.")
                print("\n1. Entrar na caverna")
                print("2. Voltar para a praia")
                
                cave_choice = get_valid_input(['1', '2'])
                
                if cave_choice == '1':
                    print_slow("\nVocê entra na caverna iluminada pela tocha...")
                    print_slow("Seguindo o mapa, você encontra uma passagem secreta...")
                    print_slow("E lá está! O tesouro lendário!")
                    return "Parabéns! Você encontrou o tesouro e completou sua missão!"
            else:
                print_slow("\nVocê sobe o penhasco mas não consegue ver muito...")
                print_slow("Talvez você precise de equipamento adequado para explorar melhor.")
                
        input("\nPressione ENTER para continuar...")

def main():
    while True:
        introduction()
        result = play_game()
        
        clear_screen()
        print_slow(f"\n{result}")
        
        print_slow("\nDeseja jogar novamente?")
        print("\n1. Sim")
        print("2. Não")
        
        if get_valid_input(['1', '2']) == '2':
            print_slow("\nObrigado por jogar! Até a próxima aventura!")
            break

if __name__ == "__main__":
    main()
