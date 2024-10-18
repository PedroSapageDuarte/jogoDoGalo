# Função para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Função para verificar se há um vencedor
def check_winner(board, player):
    # Verifica linhas, colunas e diagonais
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Função para verificar se o tabuleiro está cheio (empate)
def check_full(board):
    return all([spot != " " for row in board for spot in row])

# Função principal do jogo
def play_game():
    # Inicialização do tabuleiro 3x3
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Jogador {current_player}, é a sua vez.")
        
        # Entrada do jogador
        try:
            row, col = map(int, input("Escolha a linha e a coluna (0, 1, 2 separados por espaço): ").split())
            if board[row][col] != " ":
                print("Espaço já ocupado. Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Escolha números entre 0 e 2.")
            continue

        # Atualiza o tabuleiro com o movimento
        board[row][col] = current_player
        
        # Verifica se há vencedor
        if check_winner(board, current_player):
            print_board(board)
            print(f"Parabéns! O jogador {current_player} venceu!")
            break
        
        # Verifica se há empate
        if check_full(board):
            print_board(board)
            print("Empate!")
            break

        # Alterna entre os jogadores
        current_player = "O" if current_player == "X" else "X"

# Executar o jogo
if __name__ == "__main__":
    play_game()
