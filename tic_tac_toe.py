# 1. Инициализация игры
game = True
game_complete = False
# 2. Инициализация игрока
player = "X"
# 3. Победитель
winner = None
# 4. Создание игрового поля
field = [["-" , "-" , "-"],
        ["-" , "-", "-"],
        ["-" , "-" , "-"]]

def print_field(field):
    print("  0   1   2")
    print("0", field[0][0], "|" , field[0][1], "|" , field[0][2])
    print("1", field[1][0], "|" , field[1][1], "|" , field[1][2])
    print("2", field[2][0], "|" , field[2][1], "|" , field[2][2])

# print_field(field)

# 5. Совершение хода. Ввод номера ячейки и проверка на совпадение номера с допустимым диапазоном и на то, что ячейка свободна
def make_A_move(field):
    global player
    while True:
        move = input("Введите координаты ячейки через пробел (формат ввода: x y): ").split()

        if len(move) != 2:
            print("Введите две координаты")
            continue
        if not(move[0].isdigit() and move[1].isdigit()):
            print("Введите число")
            continue
        x, y = map(int, move) 

        if not (x >=0 and x <=2 and y >=0 and y <= 2):
            print("Введённые координаты ячейки находятся вне допустимого диапазона")
            continue
        if field[x][y] != "-":
            print("Ячейка занята")
            continue
               
        break
    field[x][y] = player 
   


# 6. Условия победы
def win_conditions(field):
    global winner
    if field[0][0] == field[0][1] == field[0][2] and field[0][0] != "-": #первый ряд
        winner = field[0][0]
        return True
    elif field[1][0] == field[1][1] == field[1][2] and field[1][0] != "-": #второй ряд
        winner = field[1][2]
        return True
    elif field[2][0] == field[2][1] == field[2][2] and field[2][0] != "-": #третий ряд
        winner = field[2][2]
        return True
    elif field[0][0] == field[1][0] == field[2][0] and field[0][0] != "-": #первая колонка
        winner = field[0][0]
        return True
    elif field[0][1] == field[1][1]== field[2][1]and field[0][1] != "-": #вторая колонка
        winner = field[0][1]
        return True
    elif field[0][2] == field[1][2] == field[2][2] and field[0][2] != "-": #третья колонка
        winner = field[0][2] 
        return True  
    elif field[0][0] == field[1][1] == field[2][2] and field[0][0] != "-": #первая диагональ
        winner = field[0][0]
        return True
    elif field[0][2] == field[1][1] == field[2][0] and field[2][0] != "-": #вторая диагональ
        winner = field[0][2]
        return True

# 7. Условия ничьи
def tie_cond(field):
    global game    
    if "-" not in field[0] and "-" not in field[1] and "-" not in field[2]:
        print("Ничья")
        print_field(field)        
        game = False

# 8. Проверка выполнения условия победы
def check_cond(field):
    global game    
    if win_conditions(field):
        print(f"Победил {winner}")
        print_field(field)        
        game = False

# 9. Смена игрока
def change_player():
    global player
    if player == "X":
        player = "0"
    else:
        player = "X"

# 10. Главная фукнция. Инициализация игрового процесса.
def GAME(field):
    while game:
        print_field(field)
        make_A_move(field)    
        check_cond(field)
        tie_cond(field)
        change_player()
    
GAME(field)