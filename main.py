board = list(range(1,10))

def board_draw(board):
    print('-'*19)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-"*19)


def input_x_o(token_of_player):
    check = False
    while not check:
        player_input = (input(f"Введите число,куда вы поставите {token_of_player} ?"))
        try:
            player_input = int(player_input)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
        if 1<=player_input<=9:
            if (str(board[player_input - 1]) not in "XO"):
                board[player_input - 1] = token_of_player
                check = True
            else:
                print("Уже занята, займите другую")
        else:
            print("Ваше число не в промежутке от 1 до 9")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for x in win_coord:
       if board[x[0]] == board[x[1]] == board[x[2]]:
          return board[x[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        board_draw(board)
        if counter % 2 == 0:
           input_x_o("X")
        else:
           input_x_o("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    board_draw(board)
main(board)

input("Нажмите Enter для выхода!")