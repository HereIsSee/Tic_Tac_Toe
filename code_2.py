import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" "]*3 for _ in range(3)]
        self.buttons = []

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=3, font=("Helvetica", 20),
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(row, col):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, row, col):
        player = self.board[row][col]
        return all([self.board[row][j] == player for j in range(3)]) or \
               all([self.board[i][col] == player for i in range(3)]) or \
               all([self.board[i][i] == player for i in range(3)]) or \
               all([self.board[i][2 - i] == player for i in range(3)]) or \
               (row == col and all([self.board[i][i] == player for i in range(3)])) or \
               (row + col == 2 and all([self.board[i][2 - i] == player for i in range(3)]))

    def is_board_full(self):
        return all([cell != " " for row in self.board for cell in row])

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text="")
        self.current_player = "X"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
