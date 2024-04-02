from random import randint

#bombs_placed = 0
bombs = 0
Layout = []
shown_Layout = []
title = f'\033[21m          \033[0m \n\033[21mMINESEATER\033[0m'
rules = f'\033[3meg. (0,1) -> 01\033[0m'

print(title + '\n')
print(rules)

length = int(input('\nPlease select a grid size(recommended 3-7)\n<grid-size> '))
#bombs = int(input('\nPlease set the number of bombs\n<bombs> '))

class field:
    def __init__(self,coord,bomb,bomb_nearby,checked,detected):
        self.coord = coord
        self.bomb = bomb
        self.bomb_nearby = bomb_nearby
        self.checked = checked
        self.detected = detected

t_f = {1 : True,0 : False,2: False}

def bomb_check(l,m):
    if Layout[l][m].bomb:
        Layout[l][m].bomb_nearby = "/"
        return
    if Layout[l][m].coord[0] > 0:
        if Layout[l-1][m].bomb:
            Layout[l][m].bomb_nearby += 1
    if Layout[l][m].coord[1] > 0:
        if Layout[l][m-1].bomb:
            Layout[l][m].bomb_nearby += 1
    if Layout[l][m].coord[0] < (length - 1):
        if Layout[l+1][m].bomb:
            Layout[l][m].bomb_nearby += 1
    if Layout[l][m].coord[1] < (length - 1):
        if Layout[l][m+1].bomb:
            Layout[l][m].bomb_nearby += 1


for i in range(length):
    Layout.append([])
    shown_Layout.append([])
    for k in range(length):
        Layout[i].append(None)
        shown_Layout[i].append(None)

for i in range(length):
    for k in range(length):
        Layout[i][k] = field((i,k),t_f[randint(0,2)],0,False,False)
        shown_Layout[i][k] = (i,k)

def bomb_define_again():
    for i in range(length):
        Layout.append([])
        shown_Layout.append([])
        for k in range(length):
            Layout[i].append(None)
            shown_Layout[i].append(None)

    for i in range(length):
        for k in range(length):
            Layout[i][k] = field((i,k),t_f[randint(0,2)],0,False,False)
            shown_Layout[i][k] = (i,k)

    for i in range(length):
        for k in range(length):
            bomb_check(i,k)

for i in range(length):
    for k in range(length):
        bomb_check(i,k)

for i in range(length):
    for k in range(length):
        if Layout[i][k].bomb:
            bombs += 1
while bombs == 0:
    bomb_define_again()

print(f'\nbombs : {bombs}')

def end(win):
    print("\nDas Spiel ist vorbei!\n")
    if win == False:
        print("Du hast verloren!")
    if win == True:
        print("Du hast gewonnen!\n")
    input()

def game(show):
    output = ""
    for i in range(length):
        output += f'{shown_Layout[i]}\n'
        if show:
            for k in range(length):
                print(f'{Layout[i][k].coord} {Layout[i][k].bomb} {Layout[i][k].bomb_nearby}')

    print(f'\n{output}')
    check_field()


def check_field():
    check = input('<mineseater> ')
    go_on = 0
    bombs_detected = 0
    if check == "show":
        game(True)
    else:
        try:
            for i in range(length):
                for k in range(length):
                    if int(check[0]) == Layout[i][k].coord[0] and int(check[1]) == Layout[i][k].coord[1]:
                        Layout[i][k].checked == True
                        if Layout[i][k].bomb == True:
                            end(False)
                            return
                        if Layout[i][k].bomb == False:
                            print(f"Anliegende Bomben: {Layout[i][k].bomb_nearby}\n")
                            Layout[i][k].checked = True
                    if Layout[i][k].checked == True or Layout[i][k].bomb_nearby == "/":
                        go_on += 1
                    else:
                        pass
                    if Layout[i][k].checked == True and Layout[i][k].bomb == True:
                        bombs_detected += 1
                    else:
                        pass
            if go_on >= (length**2):
                end(True)
            elif bombs_detected == bombs:
                end(True)
            else:
                check_field()
        except:
            print(f"input error >>>{check}<<< please try again ")
            check_field()




if __name__ == "__main__":
    game(False)
