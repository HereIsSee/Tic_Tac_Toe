def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        player_input = input("Player {} enter your move (row col): ".format(players[current_player])).split()
        row, col = map(int, player_input)
        if board[row][col] == " ":
            board[row][col] = players[current_player]
            if check_win(board, players[current_player]):
                print_board(board)
                print("Player {} wins!".format(players[current_player]))
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = (current_player + 1) % 2
        else:
            print("Invalid move. Try again.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        tic_tac_toe()

if __name__ == "__main__":
    tic_tac_toe()
