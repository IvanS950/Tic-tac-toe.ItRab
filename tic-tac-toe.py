play_field = [1, 2, 3,
              4, 5, 6,
              7, 8 ,9]
pf = play_field

def pf_map():
    print(pf[0], end=" ")
    print(pf[1], end=" ")
    print(pf[2])

    print(pf[3], end=" ")
    print(pf[4], end=" ")
    print(pf[5])

    print(pf[6], end=" ")
    print(pf[7], end=" ")
    print(pf[8])

# Победные комбинации
win_comb = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]

# Ход
def step_pf(step, icon):
    ind = pf.index(step)
    pf[ind] = icon

# Результат игры
def get_result():
    win = ""
    for i in win_comb:
        if pf[i[0]] == "x" and pf[i[1]] == "x" and pf[i[2]] == "x":
            win = "Игрок 1"
        elif pf[i[0]] == "o" and pf[i[1]] == "o" and pf[i[2]] == "o":
            win = "Игрок 2"
    return win

game_over = False
player = True

while game_over == False:
    pf_map()
    # Ход игрока
    if player == True:
        icon = "x"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        icon = "o"
        step = int(input("Игрок 2, ваш ход: "))

    step_pf(step, icon)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player = not (player)

# Игра окончена. Покажем карту. Объявим победителя.
pf_map()
print("Победил", win)