def print_field(field):
    print("---------")
    print("| " + field[0] + " " + field[1] + " " + field[2] + " |")
    print("| " + field[3] + " " + field[4] + " " + field[5] + " |")
    print("| " + field[6] + " " + field[7] + " " + field[8] + " |")
    print("---------")


def dimension_field(field):
    return [[field[i+n] for i in range(3)] for n in range(0,9,3)]


def flat_list(field):
    return [item for sublist in field_[::-1] for item in sublist]


def check_field(field):
    x_wins = False
    o_wins = False
    combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for x in range(8):
        row = []
        for y in range(3):
            row.append(field[combos[x][y]])
        if row.count('X') == len(row):
            x_wins = True
        if row.count('O') == len(row):
            o_wins = True

    if x_wins:
        print("X wins")
        return True
    elif o_wins:
        print("O wins")
        return True
    elif field.count('_') == 0:
        print("Draw")
        return True
    else:
        return False


field = "_________"
field_ = dimension_field(field)[::-1]
print_field(field)
turn_X = True

while True:
    print("Enter the coordinates: ")
    coord = input()
    if len(coord.split()) == 2 and coord.split()[0].isdigit() and coord.split()[1].isdigit():
        x = int(coord.split()[0])
        y = int(coord.split()[1])
        if 0 < x < 4 and 0 < y < 4:
            if field_[y-1][x-1] == 'X' or field_[y-1][x-1] == 'O':
                print("This cell is occupied! Choose another one!")
            else:
                mark = 'X' if turn_X else 'O'
                field_[y - 1][x - 1] = mark
                turn_X = not turn_X
                print_field(flat_list(field_))
                if check_field(flat_list(field_)):
                    break
        else:
            print("Coordinates should be from 1 to 3!")
    else:   
        print("You should enter numbers!")