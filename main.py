from random import choice
from sys import exit

#* Main Game
class spot():
    def __init__(self,index,coord,bomb,adjacent_bombs):
        self.index = index
        self.coord = coord
        self.bomb = bomb
        self.adjacent_bombs = adjacent_bombs
    
    def check_bomb(self,index: int) -> str:
        if self.bomb == True:
            field_out_list[index] = "☒"
            print_field()
            end_game(False)
        else:
            return self.adjacent_bombs

    def __repr__(self) -> str:
        return str(f">{self.coord} {self.bomb} {self.adjacent_bombs}<")

def main() -> None:
    global grid_size,field,coords_list,field_out_list,bombs
    print("\x1b[2J\x1b[H",end="")
    grid_size = ask_size()
    bombs = ask_bombs()

    field = []
    index = 0
    index_list = []
    coords_list = []
    for i in range(grid_size):
        field.append([])
        for k in range(grid_size):
            field[i].append(spot(index,(i,k),False,0))
            index += 1
            coords_list.append(f"{field[i][k].coord[0]}{field[i][k].coord[1]}")
    
    for i in range(index):
        index_list.append(i)
    for i in range(bombs):
        made_choice = choice(index_list)
        index_list.remove(made_choice)
        for k in field:
            for h in k:
                if int(h.index) == int(made_choice):
                    h.bomb = True

    for i in range(len(field)):
        for k in range(len(field[i])):
            #! Vertical
            if field[i][k].coord[0] > 0:
                if field[i-1][k].bomb == True:
                    field[i][k].adjacent_bombs += 1
            if field[i][k].coord[0] < grid_size-1:
                if field[i+1][k].bomb == True:
                    field[i][k].adjacent_bombs += 1
            #! Horizontal
            if field[i][k].coord[1] > 0:
                if field[i][k-1].bomb == True:
                    field[i][k].adjacent_bombs += 1
            if field[i][k].coord[1] < grid_size-1:
                if field[i][k+1].bomb == True:
                    field[i][k].adjacent_bombs += 1

    field_out_list = []
    for _ in range(grid_size**2):
        field_out_list.append("☐")
    print_field()
    game_loop()

def print_field() -> None:
    print("\x1b[2J\x1b[H",end="")
    field_out = "  "
    index = 0
    for i in range(grid_size):
        field_out += f"\x1b[2m{i}\x1b[0m  "
    for i in range(grid_size):
        field_out += f"\n\x1b[2m{i}\x1b[0m "
        for k in range(grid_size):
            field_out += f"{field_out_list[index]}  "
            index += 1
    print(field_out)

def game_loop() -> None:
    while True:
        txt = input(">")
        if txt == "exit":
            exit()
        elif txt in coords_list:
            for i in range(len(field)):
                for k in range(len(field[i])):
                    if txt == f"{field[i][k].coord[1]}{field[i][k].coord[0]}":
                        field_out_list[field[i][k].index] = f"{field[i][k].check_bomb(field[i][k].index)}"
            print_field()
            free = 0
            for i in field_out_list:
                if i == "☐":
                    free += 1
            if free == bombs:
                end_game(True)
        else:
            print_field()

#* Define Vars
def ask_size() -> int:
    txt = 0
    while txt not in [2,3,4,5,6,7,8,9]:
        txt = input("How big should the field be? (3-5 is recommended)\n>")
        try:
            txt = int(txt)
            if txt < 2 or txt > 9:
                print(f"\x1b[A\x1b[K>{txt} --Error")
        except:
            txt = txt
            print(f"\x1b[A\x1b[K>{txt} --Error")
    print("\x1b[2J\x1b[H",end="")
    return txt

def ask_bombs() -> int:
    txt = 0
    while txt > (grid_size**2)-1 or txt < 1 or type(txt) != int:
        txt = input(f"How many bombs should the field have? (grid:{grid_size}x{grid_size} / {grid_size**2} spots)\n>")
        try:
            txt = int(txt)
            if txt > (grid_size**2)-1 or txt < 1:
                print(f"\x1b[A\x1b[K>{txt} --Error")
        except:
            txt = txt
            print(f"\x1b[A\x1b[K>{txt} --Error")
            txt = 0
    return txt

def end_game(win: bool) -> None:
    if win == True:
        print("You have won the game!")
        exit()
    else:
        print("You have lost the game!")
        exit()

#* Start
if __name__ == "__main__":
    main()