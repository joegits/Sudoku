from random import randint
import csv

empty = [0,0,0,0,0,0,0,0,0]
columns = [[],[],[],[],[],[],[],[],[]]
squares = [[],[],[],[],[],[],[],[],[]]

print("This program will generate sodukko-boards and save them in a separate file.\n")

def make_squares(a):
    if len(squares[0]) < 9:
        for i in a:
            if i in (a[0:3]):
                squares[0].append(i)
    
            if i in (a[3:6]):
                squares[1].append(i)
    
            if i in (a[6:9]):
                squares[2].append(i)
    
    elif len(squares[3]) < 9:
        for i in a:
            if i in (a[0:3]):
                squares[3].append(i)
    
            if i in (a[3:6]):
                squares[4].append(i)
    
            if i in (a[6:9]):
                squares[5].append(i)

    elif len(squares[6]) < 9:
        for i in a:
            if i in (a[0:3]):
                squares[6].append(i)
    
            if i in (a[3:6]):
                squares[7].append(i)
    
            if i in (a[6:9]):
                squares[8].append(i)

    
def test_square(seq):
    complete = True
    length = len(columns[0])
    if length < 3:
        if (seq[0] in squares[0]) or (seq[1] in squares[0]) or (seq[2] in squares[0]):
            complete = False
        elif (seq[3] in squares[1]) or (seq[4] in squares[1]) or (seq[5] in squares[1]):
            complete = False
        elif (seq[6] in squares[2]) or (seq[7] in squares[2]) or (seq[8] in squares[2]):
            complete = False
        
    elif 3 <= length < 6:
        if (seq[0] in squares[3]) or (seq[1] in squares[3]) or (seq[2] in squares[3]):
            complete = False
        elif (seq[3] in squares[4]) or (seq[4] in squares[4]) or (seq[5] in squares[4]):
            complete = False
        elif (seq[6] in squares[5]) or (seq[7] in squares[5]) or (seq[8] in squares[5]):
            complete = False
    
    elif 6 <= length:
        if (seq[0] or seq[1] or seq[2]) in squares[6]:
            complete = False
        elif (seq[3] or seq[4] or seq[5]) in squares[7]:
            complete = False
        elif (seq[6] or seq[7] or seq[8]) in squares[8]:
            complete = False
    else:
        print("fel fel fel")
    
    return complete

def test_row(seq):
    #counter = 0
    k = 0
    complete = True
    for i in seq:
        if i in columns[k]:
            #counter += 1
            complete = False
            
        k += 1
    #if counter == 0:
        #complete = True
    #else:
        #complete = False
    return complete

aotg = [202, 207, 211, 197, 198, 128, 200, 193, 199, 199, 210, 197, 206]

def gn():
    
    testar = 0
    sequence = []
    while True:
        number = (randint(1,9))
        if number not in sequence:
            sequence.append(number)
        if sum(sequence[0:10]) == 45:
            testseq = test_row(sequence)
            testsquare = test_square(sequence)
            if testseq == False or testsquare == False:
                testar += 1
                sequence = []
            
                
                if testar > 200000:
                     break
                    
            else:
                for addv in range(9):
                    columns[addv].append(sequence[addv])
                make_squares(sequence)
                break
           
    return sequence
    
def gn2():
    
    testar = 0
    sequence = []
    while testar < 9:
        number = 45 - sum(columns[testar])
        if number not in sequence:
            sequence.append(number)
        if sum(sequence[0:10]) == 45:
            testseq = test_row(sequence)
            testsquare = test_square(sequence)
            if testseq == False or testsquare == False:
                testar += 1
                sequence = []
                
            
                
                if testar % 100 == 0:
                    print(testar)
                    print("fel")
                    
            else:
                for addv in range(9):
                    columns[addv].append(sequence[addv])
                make_squares(sequence)
                break
        testar +=1
           
    return sequence
     
        
cykels = 1
amount = int(input("How many boards do you want to generate? \n"))

while cykels <= amount:           
    empty = [0,0,0,0,0,0,0,0,0]
    columns = [[],[],[],[],[],[],[],[],[]]
    squares = [[],[],[],[],[],[],[],[],[]]
    
    
    board = [(gn()),(gn()),(gn()),(gn()),(gn()),(gn()),(gn()),(gn()),(gn2())]


    if sum(board[8]) == 45:
        print("Board {}".format(cykels))
        for i in board:
            print(i)
        cykels += 1
        with open('sudokuboards.csv', 'a+') as csvfile:
            filewriter = csv.writer(csvfile)
# delimiter=',')
            filewriter.writerow(board)
            
            

    