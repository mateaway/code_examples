import math
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

# Функция для отображения игрового поля с цветами
def print_board(board):
    for row in board:
        colored_row = []
        for cell in row:
            if cell == "X":
                colored_row.append(Fore.RED + "X" + Style.RESET_ALL)
            elif cell == "O":
                colored_row.append(Fore.BLUE + "O" + Style.RESET_ALL)
            else:
                colored_row.append(" ")
        print(" | ".join(colored_row))
        print("-" * 9)

# Проверка победителя
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

# Проверка на ничью
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Алгоритм Minimax
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

# Ход компьютера
def computer_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

# Основной игровой цикл
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print(Fore.GREEN + "Добро пожаловать в игру 'Крестики-нолики'!")
    print(Fore.YELLOW + "Вы играете за " + Fore.RED + "'X'" + Fore.YELLOW + ", компьютер — за " + Fore.BLUE + "'O'" + Fore.YELLOW + ".")
    print_board(board)

    while True:
        # Ход игрока
        while True:
            try:
                player_move = input(Fore.CYAN + "Введите ваш ход (строка и столбец через пробел, например, '1 1'): ")
                row, col = map(int, player_move.split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print(Fore.YELLOW + "Эта клетка уже занята. Попробуйте снова.")
            except (ValueError, IndexError):
                print(Fore.YELLOW + "Некорректный ввод. Введите два числа от 0 до 2 через пробел.")

        print_board(board)
        if check_winner(board) == "X":
            print(Fore.GREEN + "Поздравляем! Вы победили!")
            break
        if is_draw(board):
            print(Fore.YELLOW + "Ничья!")
            break

        # Ход компьютера
        print(Fore.CYAN + "Ход компьютера...")
        computer_move(board)
        print_board(board)
        if check_winner(board) == "O":
            print(Fore.RED + "Компьютер победил. Удачи в следующий раз!")
            break
        if is_draw(board):
            print(Fore.YELLOW + "Ничья!")
            break

# Запуск игры
if __name__ == "__main__":
    play_game()
