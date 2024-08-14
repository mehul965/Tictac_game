import tkinter as tk
import numpy as np
import random

class TicTacToeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("400x450")
        self.configure(bg='black')

        self.board = np.full((3, 3), None)
        self.current_player = "X"
        self.game_over = False

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=400, height=400, bg='black')
        self.canvas.pack()

        self.status_label = tk.Label(self, text="", bg='black', fg='white', font=('Arial', 24))
        self.status_label.pack(pady=10)

        # Draw grid
        self.canvas.create_line(133, 0, 133, 400, fill="blue", width=5)
        self.canvas.create_line(267, 0, 267, 400, fill="blue", width=5)
        self.canvas.create_line(0, 133, 400, 133, fill="blue", width=5)
        self.canvas.create_line(0, 267, 400, 267, fill="blue", width=5)
        
        self.canvas.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        if self.game_over:
            return

        row, col = event.y // 133, event.x // 133
        
        if self.board[row, col] is None:
            self.make_move(row, col, self.current_player)
            if self.check_winner():
                self.show_winner(self.current_player)
                return
            elif self.check_draw():
                self.show_draw()
                return

            self.current_player = "O"
            self.computer_move()
            if self.check_winner():
                self.show_winner(self.current_player)
                return
            elif self.check_draw():
                self.show_draw()
                return

            self.current_player = "X"

    def make_move(self, row, col, player):
        self.board[row, col] = player
        self.draw_symbol(row, col, player)

    def draw_symbol(self, row, col, player):
        x_start = col * 133
        y_start = row * 133

        if player == "X":
            self.canvas.create_line(x_start + 20, y_start + 20, x_start + 113, y_start + 113, fill="red", width=10)
            self.canvas.create_line(x_start + 20, y_start + 113, x_start + 113, y_start + 20, fill="red", width=10)
        else:
            self.canvas.create_oval(x_start + 20, y_start + 20, x_start + 113, y_start + 113, outline="cyan", width=10)

    def computer_move(self):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.board[row, col] is None]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col, self.current_player)

    def check_winner(self):
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] and self.board[i, 0] is not None:
                return True
            if self.board[0, i] == self.board[1, i] == self.board[2, i] and self.board[0, i] is not None:
                return True
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] and self.board[0, 0] is not None:
            return True
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] and self.board[0, 2] is not None:
            return True
        return False

    def check_draw(self):
        return all(self.board[row, col] is not None for row in range(3) for col in range(3))

    def show_winner(self, player):
        self.status_label.config(text=f"Player {player} wins!")
        self.canvas.unbind("<Button-1>")
        self.game_over = True
        self.create_reset_button()

    def show_draw(self):
        self.status_label.config(text="It's a draw!")
        self.canvas.unbind("<Button-1>")
        self.game_over = True
        self.create_reset_button()

    def create_reset_button(self):
        reset_button = tk.Button(self, text="Play Again", command=self.reset_game)
        reset_button.pack()

    def reset_game(self):
        self.board = np.full((3, 3), None)
        self.current_player = "X"
        self.game_over = False
        self.canvas.delete("all")
        self.status_label.config(text="")
        self.create_widgets()

if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop()
