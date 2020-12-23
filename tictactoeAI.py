from random import choice


class TicTacToe:
    def __init__(self):
        self.turn_X = True  # X will always start the game
        self.field = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']  # start with empty field

    def __str__(self):
        return f"---------\n" \
               f"| {self.field[0][0]} {self.field[0][1]} {self.field[0][2]} |\n" \
               f"| {self.field[1][0]} {self.field[1][1]} {self.field[1][2]} |\n" \
               f"| {self.field[2][0]} {self.field[2][1]} {self.field[2][2]} |\n" \
               "---------"

    def win_combos(self):
        return {'0 0, 0 1, 0 2': "".join(self.field[0]),
                '1 0, 1 1, 1 2': "".join(self.field[1]),
                '2 0, 2 1, 2 2': "".join(self.field[2]),
                '0 0, 1 0, 2 0': "".join([row[0] for row in self.field]),
                '0 1, 1 1, 2 1': "".join([row[1] for row in self.field]),
                '0 2, 1 2, 2 2': "".join([row[2] for row in self.field]),
                '0 0, 1 1, 2 2': "".join([self.field[0][0], self.field[1][1], self.field[2][2]]),
                '0 2, 1 1, 2 0': "".join([self.field[0][2], self.field[1][1], self.field[2][0]])}

    def continue_game(self):
        x_wins = False
        o_wins = False
        if "XXX" in self.win_combos().values():
            x_wins = True
        if "OOO" in self.win_combos().values():
            o_wins = True
        if x_wins and not o_wins:
            print("X wins")
            self.field = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
            return False
        elif o_wins and not x_wins:
            print("O wins")
            self.field = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
            return False
        elif self.field[0].count('_') == 0 and self.field[1].count('_') == 0 and self.field[2].count('_') == 0:
            print("Draw")
            self.field = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
            return False
        else:
            return True

    def easy_ai_move(self, mark):
        free_cells = [[i, j] for i in range(3) for j in range(3) if self.field[i][j] == '_']
        cell = choice(free_cells)
        y = cell[0]
        x = cell[1]
        self.field[y][x] = mark

    def medium_ai_move(self, mark):
        if mark == 'X': other_mark = 'O'
        else: other_mark = 'X'
        for key in self.win_combos():
            row = self.win_combos()[key]
            if row.count(mark) == 2 and row.count('_') == 1:
                pos = row.find('_')
                y = int(key.split(',')[pos].split()[0])
                x = int(key.split(',')[pos].split()[1])
                self.field[y][x] = mark
                return
        for key in self.win_combos():
            row = self.win_combos()[key]
            if row.count(other_mark) == 2 and row.count('_') == 1:
                pos = row.find('_')
                y = int(key.split(',')[pos].split()[0])
                x = int(key.split(',')[pos].split()[1])
                self.field[y][x] = mark
                return
        self.easy_ai_move(mark)

    def hard_ai_move(self, mark):
        self.medium_ai_move(mark)

    def score(self, depth, mark):
        if mark == 'X': other_mark = 'O'
        else: other_mark = 'X'
        if mark*3 in self.win_combos().values():
            return 10 - depth
        elif other_mark*3 in self.win_combos().values():
            return depth - 10
        else:
            return 0

    def player_move(self, mark):
        while True:
            cell = input("Enter the coordinates: ")
            if len(cell.split()) == 2 and cell.split()[0].isdigit() and cell.split()[1].isdigit():
                y = int(cell.split()[0]) - 1
                x = int(cell.split()[1]) - 1
                if 0 <= x < 3 and 0 <= y < 3:
                    if self.field[y][x] == 'X' or self.field[y][x] == 'O':
                        print("This cell is occupied! Choose another one!")
                    else:
                        self.field[y][x] = mark
                        return
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")


game = TicTacToe()
commands = ["easy", "medium", "hard", "user"]
while True:
    cmd = input("Input command: ")
    cmds = cmd.split()
    if cmd == 'exit':
        exit()
    elif len(cmds) == 3 and cmds[0] == 'start' and cmds[1] in commands and cmds[2] in commands:
        while game.continue_game():
            if game.turn_X:
                if cmd.split()[1] == 'easy':
                    print('Making move level "easy"')
                    game.easy_ai_move('X')
                elif cmd.split()[1] == 'medium':
                    print('Making move level "medium"')
                    game.medium_ai_move('X')
                elif cmd.split()[1] == 'hard':
                    print('Making move level "hard"')
                    game.hard_ai_move('X')
                elif cmd.split()[1] == 'user':
                    game.player_move('X')
            else:
                if cmd.split()[2] == 'easy':
                    print('Making move level "easy"')
                    game.easy_ai_move('O')
                elif cmd.split()[2] == 'medium':
                    print('Making move level "medium"')
                    game.medium_ai_move('O')
                elif cmd.split()[2] == 'hard':
                    print('Making move level "hard"')
                    game.hard_ai_move('O')
                elif cmd.split()[2] == 'user':
                    game.player_move('O')
            print(game)
            game.turn_X = not game.turn_X
    else:
        print("Bad parameters!")

