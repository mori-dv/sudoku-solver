
sudoku = list()


def get_sudoku():
    print("please enter sudoku elements in 9 cols and seperated by space")
    for i in range(9):
        sudoku.append(list(map(int, input().split())))


def draw():

    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            print(sudoku[i][j], end=" ")
        print()


def find_free_place():

    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                return i, j
    return False


def is_valid(n, x, y):

    for i in range(9):
        if sudoku[x][i] == n or sudoku[i][y] == n:
            return False

    x_corner = (x // 3) * 3
    y_corner = (y // 3) * 3
    for xc in range(x_corner, x_corner + 3):
        for yc in range(y_corner, y_corner + 3):
            if sudoku[xc][yc] == n:
                return False
    return True


def solve():

    if find_free_place() is False:
        return True
    else:
        x, y = find_free_place()

    for i in range(1, 10):
        if is_valid(i, x, y):
            sudoku[x][y] = i
            if solve():
                return True
            sudoku[x][y] = 0
    return False


if __name__ == "__main__":
    print("Hello, this is a sudoku solver program which solve any sudoku table with backtrace")
    get_sudoku()

    if solve():
        print("+++++++++++++++ THE SOLVED SUDOKU +++++++++++++++")
        draw()
    else:
        print("I Cannot solve it =///")

