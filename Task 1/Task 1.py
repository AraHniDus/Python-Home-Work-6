X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct(): #Выводит на экран инструкцию для игрока.
    print(
        """
       Приветствую тебя бесстрашный игрок, осмелишься ли ты бросить вызов бездушной машине в 
       интеллектуальной игре "Крестики-нолики".
       Чтобы сделать ход, введи число от 0 до 8. 
       Числа однозначно соответствуют полям доски - так, как показано ниже:

                           0 | 1 | 2
                           ---------
                           3 | 4 | 5
                           ---------
                           6 | 7 | 8

       Приготовься к сражению и прибудет с тобой сила!\n
       """
    )

def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces(): #Определяет принадлежность перового хода.
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (y, n): ")
    if go_first == "y":
        print("\nНу что ж, желаю удачи: играй крестиками.")
        player = X
        computer = O
    else:
        print("\nТвоя уверенность тебя погубит... Начинает компьютер.")
        computer = X
        player = O
    return computer, player

def new_board(): #Создаёт новую игровую доску.
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board): #Отображает игровую доску на экране.
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board): #Создаёт список доступных ходов.
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board): #Определяет победителя в игре.
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def player_move(board, player): #Получает ход игрока.
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭто поле уже занято. Выбери другое.\n")
    print("Ладно...")
    return move

def computer_move(board, computer, player): #Делает ход за компьютерного противника.
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for moves in legal_moves(board):
        board[move] = player
        if winner(board) == player:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn): #Осуществляет переход хода.
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, player): #Поздравляет победителя игры.
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Очень жаль, но тебе не удалось победить непобедимую машину.\n" \
              "Не стоит отчаиваться может быть повезет в следующий раз.")
    elif the_winner == player:
        print("Невероятно ты смог превзойти непобедимую машину и доказать свое превосходство! \n" \
              "Можешь бросить вызов компьютеру еще раз.")
    elif the_winner == TIE:
        print("Тебе почти удалось победить. \n" \
              "Попытайся еще раз может быть в следующий раз тебе повезёт.")

def main():
    display_instruct()
    computer, player = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == player:
            move = player_move(board, player)
            board[move] = player
        else:
            move = computer_move(board, computer, player)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, player)

main()
input("Нажмите Enter, чтобы выйти.")