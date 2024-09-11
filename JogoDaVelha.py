# Imprimi o tabuleiro
def print_board(board):
    print("\n")
    print("   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))
        if i < 2:
            print("  ---+---+---")
    print("\n")

# Verificar se um jogador venceu
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

# Verifica se o tabuleiro está cheio
def check_full(board):
    return all([spot != " " for row in board for spot in row])

# Main
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        # Pedir entrada do jogador
        try:
            row, col = map(int, input(f"Jogador {current_player}, insira linha e coluna (0, 1, 2): ").split())
            if board[row][col] != " ":
                print("Posição já ocupada! Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Insira números válidos (0, 1 ou 2).")
            continue
        
        # Atualizar o tabuleiro com a jogada
        board[row][col] = current_player
        
        # Verifica se o jogador atual venceu
        if check_winner(board, current_player):
            print_board(board)
            print(f"Jogador {current_player} venceu!")
            break
        
        # Verifica se deu empate
        if check_full(board):
            print_board(board)
            print("Empate!")
            break
        
        # Trocar jogado
        current_player = "O" if current_player == "X" else "X"

# Start
if __name__ == "__main__":
    tic_tac_toe()
