class Connect4:
    def __init__(self):
        self.board = [[' ']*7 for _ in range(6)]
        self.player_turn = 'X'

    def print_board(self):
        print('\n'.join([' '.join(row) for row in self.board[::-1]]))
        print('-'*29)
        print(' '.join(map(str, range(7))))

    def is_valid_move(self, col):
        return self.board[-1][col] == ' '

    def make_move(self, col):
        for row in self.board:
            if row[col] == ' ':
                row[col] = self.player_turn
                break

    def check_win(self):
        for row in range(6):
            for col in range(7):
                try:
                    if (self.board[row][col] == self.player_turn and
                        self.board[row+1][col+1] == self.player_turn and
                        self.board[row+2][col+2] == self.player_turn and
                        self.board[row+3][col+3] == self.player_turn):
                        return True
                except IndexError:
                    pass

                try:
                    if (self.board[row][col] == self.player_turn and
                        self.board[row+1][col] == self.player_turn and
                        self.board[row+2][col] == self.player_turn and
                        self.board[row+3][col] == self.player_turn):
                        return True
                except IndexError:
                    pass

        return False

    def play_game(self):
        while True:
            self.print_board()
            print(f"Player {self.player_turn}'s turn")
            move = int(input("Enter your move (0-6): "))
            if self.is_valid_move(move):
                self.make_move(move)
                if self.check_win():
                    self.print_board()
                    print(f"Player {self.player_turn} wins!")
                    break
                self.player_turn = 'O' if self.player_turn == 'X' else 'X'
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    game = Connect4()
    game.play_game()
