import csv
from sys import exit
from random import randint
indextoblank = [[],[],[],[],[],[],[],[],[]]
playableboard = []
playboard = []
check_board = []
inint = []
regret_line = ["a"]



def choose_level():
    difficulty = 0
    numbers = ("1","2","3","4","5","6","7","8","9")
    blanks_or_level = None
    level = None
    
    while blanks_or_level not in ("b","l"):
        blanks_or_level = input("Do you want to choose difficulty via number of (b)lank spaces or via (l)evel? ").casefold()
    
    if blanks_or_level == "b":
        while difficulty < 3 or difficulty > 65:
            difficulty = int(input("How many blank spaces do you want? (15-65) "))
    if blanks_or_level == "l":
        while difficulty == 0:
            level = input("\nChoose level:\n1: Very easy.\n2: Easy\n3: Medium.\n4: Hard\n5: Expert\n")
            if level == "1":
                difficulty = randint(12,21)
            if level == "2":
                difficulty = randint(24,30)
            if level == "3":
                difficulty = randint(33,40)
            if level == "4":
                difficulty = randint(44,50)
            if level == "5":
                difficulty = randint(54,61)

    return difficulty

#get random board from csv file and generate random blanks according to input.
def get_board(difficulty):
    with open('sodukoboards.csv', newline="") as f:
    
        reader = csv.reader(f)
        logs = list(reader)
        select_board = randint(0,(len(logs))-1)
        print("\nBoard:",select_board,)
    
    global check_board
    global playboard
    global original_board
    playboard = logs[select_board]
    check_board = logs[select_board]
    
    for i in playboard:
        s = i
        only_digits = "".join([c for c in s if c.isdigit()]) 
        row1 =[]
    
        for k in only_digits:
            row1.append(int(k))
        playableboard.append(row1)


        numbtodel = []
        original_board = playableboard
    while sum(numbtodel) != difficulty:
        numbtodel = []
        for i in range(9):
            numbtodel.append(randint(0,8)) 
    
    position = 0
    for i in numbtodel:
        counter = i
        while counter > 0:
            blank = randint(1,9)
            if blank in indextoblank[position]:
                continue
            indextoblank[position].append(blank)
            counter -= 1
        position += 1

    rowc = 0
    for i in numbtodel:
        for place in indextoblank[rowc]:
            playableboard[rowc][place-1] = 0
        rowc += 1

    

    check_board = playableboard
        
#transform the board to visual output.
def show_playboard(show_board):

    show_board = [[x if x != 0 else " " for x in y] for y in show_board]
    
    
    count = 1
    row_ident = ["A","B","C","D","E","F","G","H","I"]
    print("\n")
    print("   1 2 3   4 5 6   7 8 9")
    print(" " + "-" * 25)
    for i in show_board:
        print("{9}|{0:^3}{1}{2:^3}|{3:^3}{4}{5:^3}|{6:^3}{7}{8:^3}|"
.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],row_ident[count-1]))
        if count % 3 == 0:
            print(" " + "-" * 25)
        count += 1
        
def play_game():
    global regret_line
    sure = None
    while True:
        
        cord = list((input("\nChoose position by coordinate to enter number: ").casefold()))
        
        if len(cord) > 3:
           continue
        if cord[0] in ("a","b","c","d","e","f","g","h","i") and cord[-1] in ("1","2","3","4","5","6","7","8","9"):
            x = int(cord[-1])-1
            y = int(ord(cord[0]))-97
            if not check_cords(x,y):
                continue
            
            while True:
                ins_numb = input(f'\nWhat number (1-9) do you want to insert at cordinate {cord[0]}-{cord[-1]}? ')
                if ins_numb in ("1","2","3","4","5","6","7","8","9"):
                    break
            break

        elif cord[0] == "s":
            show_playboard(playableboard)
        elif cord[0] == "u":
            regret_turn()
        elif cord[0] == "t":
            check_faults()
        elif cord == ['k', 'e', 'y']:
            show_playboard(original_board)
        elif cord[0] == "q":
            print("Thank you for playing!")
            exit()
        else:
            print('\nPlease enter a valid coordinate (Example: "e5"). or choose another option:\n"u" to undo last turn.\n"s" to show board again.\n"t" to try if your solution is correct.\n...or enter "q" to quit the game.')
    #insert number
    regret_line.extend([y,x,(playableboard[y][x])])
    playableboard[y][x] =int(ins_numb)
    
            

#check if input is a valid cordinate
def check_cords(x,y):
    if check_board[y][x] == 0:
        valid = True
    else:
        valid = False
        print("This number can't be changed.")
    return valid

#regret the last input one at a time until board is at start point.    
def regret_turn():
    global playableboard
    global regret_line
    if regret_line[-1] == "a":
        print("You are at the start point of the board, you can not regret another turn.")
    else:
        rn = regret_line.pop(-1)
        rx = regret_line.pop(-1)
        ry = regret_line.pop(-1)
        playableboard[ry][rx] = rn
        show_playboard(playableboard)
    
aotg = [202, 207, 211, 197, 198, 128, 200, 193, 199, 199, 210, 197, 206]

def check_faults():
    global playableboard
    numbers = (1,2,3,4,5,6,7,8,9)
    colcheck = [[],[],[],[],[],[],[],[],[]]
    squarebuild = [[],[],[],[],[],[],[],[],[]]
    boardiscorrect = False
    rowcheck = 0
    columncheck = 0
    squarecheck = 0
    position = 0
    
    #check rows
    for i in playableboard:
        #rowok = 0
        if all(elem in i for elem in numbers):
            rowcheck += 1
            
            
                
    #build columns       
    for i in playableboard:
        for k in range(9):
            colcheck[k].append(i[k])
    #check columns
    for i in colcheck:
        if all(elem in i for elem in numbers):
            columncheck += 1

    
    #build squares
    
    for i in playableboard:
        position += 1
        for k in range(9):
            if position < 4:
                sd = int(k/3)
                squarebuild[sd].append(i[k])
            if 4 <= position < 7:
                sd = int(k/3)+3
                squarebuild[sd].append(i[k])
            if position >= 7:
                sd = int(k/3)+6
                squarebuild[sd].append(i[k])


    
    # check squares
    for i in squarebuild:
        if all(elem in i for elem in numbers):
            squarecheck += 1
    
    if (rowcheck+columncheck+squarecheck) == 27:
        boardiscorrect = True
        
    if boardiscorrect:
        print("\nYour solution is completely correct!")
    else:

        for i in playableboard:
            if " " in i:
                print("\nYou are missing some numbers!")
                break
            
        else:
            print("\nSomething is wrong...")
        
        

#program starts
print("Welcome to just another game of Sudoku!\n\nIn this game the blank spaces on the board are completely random, and the difficulty level is based on the number of empty spaces. This could actually in some cases mean that an 'easy' board is harder to play then a 'hard'. However, all boards have at least one possible solution based on the numbers provided when started!\n\nDuring the game you can change the numbers you already inserted, but you can never change a number provided at the start game. Remember that you can always undo the numbers you inserted, one at a time, by entering 'u'!\n\nLet's start!\n")

difficulty = choose_level()    
get_board(difficulty)
while True:
    show_playboard(playableboard)
    play_game()
