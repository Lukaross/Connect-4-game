"""
connect 4 game for python coursework.
name: Luka Ross
student ID: 10275181
"""
import random
import copy
import sys

col_len=7
row_len=6
chunk_len=4

def newGame(player1,player2):
    
    """
    this function creates a new game in the form of a dictionary
    """
    game = {
     'player1' : player1,
     'player2' : player2,
     'who' : 1,
     'board' : [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0] ]
     }
 
    return game
 
def printBoard(board):
    
    """
    this function takes the board as an input, copies it and changes all the 0,1,2's to X,O's and blank spaces
    and then joins them from a list to a string and prints it.
    """
    
    copy1 = copy.deepcopy(board) #makes a deepcopy of the board
    s="¦"
    print("¦1¦2¦3¦4¦5¦6¦7¦")
    print("+-+-+-+-+-+-+-+")
    for i in range(row_len):           
        for j in range(col_len):
            if copy1[i][j] == 0:
                copy1[i][j] = " "
            if copy1[i][j] == 1:
                copy1[i][j] = "X"
            if copy1[i][j] == 2:
                copy1[i][j] = "O"
        print("¦"+s.join(copy1[i])+"¦") #joins the board list into desired string format
    return 

def getValidMoves(board):
    
    """
    this function takes the board varible and returns a list of possible moves where the numbers 0-6 
    represent the coloums 1-7 on the printed board.
    which ever ith coloum does not have a 0 in the top row, the ith number from 0-6 is removed from the list.
    """
    
    pos_moves = [0,1,2,3,4,5,6]
    for i in range(7):
        if board[0][i] != 0:
            pos_moves.remove(i)
    return pos_moves

def makeMove(board,move,who):
    
    """
    this function takes board varible and changes the entry whoses number and coloum depend on move and who. 
    it then returns the board.
    """
    
    for i in reversed(range(0,6)):
        if board[i][move] == 0:
            board[i][move] = who
            break    
    return board

def hasWon(board,who):
    
    """
    this function checks if a player has won the game
    it takes the varible 'board' and checks for the number 'who' 4 times in a row vetically, horizontally and diagonally.
    it returns true if player 'who' has won and false otherwise    
    """    
    #vetrical check 
    for y in range(3):
        for x in range(7):
            if board[y][x] == who and board[y+1][x] == who and board[y+2][x] == who and board[y+3][x]==who:
                return True
    
            
    #horizontal check
    for y in range(6):
        for x in range(4):
            if board[y][x] == who and board[y][x+1] == who and board[y][x+2] == who and board[y][x+3]==who:
                return True
    

    #diagonal check /
    for y in range(3):
        for x in range(3,7):
            if board[y][x] == who and board[y+1][x-1] == who and board[y+2][x-2] == who and board[y+3][x-3]==who:
                return True
    

    #diagonal check \
    for y in range(3):
        for x in range(4):
            if board[y][x] == who and board[y+1][x+1] == who and board[y+2][x+2] == who and board[y+3][x+3]==who:
                return True
    
    
    return False 

def suggestMove1(board,who):
    '''
    This function suggests a move for a computer player
    takes a varible board and who and checks the board for winning moves.
    if there is a winning move for the computer or the opponent it returns that move,
    otherwise it plays the first available move.
    '''
    
    #assigns player and oppoent based on whos turn it is 
    if who == 1:
        player = 1 
        opponent = 2
    else:
        player = 2
        opponent = 1   
    #suggests a move to win    
    if has_winning_move(board,player) != 7:
        return has_winning_move(board,player)
    #makes a valid move         
    elif has_winning_move(board,player) == 7 and has_winning_move(board,opponent) == 7:
        return getValidMoves(board)[0]
    #suggests a move to block        
    else:
        return has_winning_move(board,opponent)            
    
def has_winning_move(board,who):
    '''
    this is a helper function for suggest move, it checks the board to see
    if there are any moves that would result in a win.
    it does this by making all valid moves and checking which result in a hasWon == True.
    '''
    #makes a deepcopy of the board
    copy2 = copy.deepcopy(board)
    valid_moves = getValidMoves(board)
    #checks all valid moves to see which one results in a win
    for n in range(len(valid_moves)): 
        copy2 = makeMove(copy2,valid_moves[n],who)
        if hasWon(copy2,who) == True:
            return valid_moves[n]
        copy2 = copy.deepcopy(board)
     #returning 7 means there is no winning move
    return 7

def play():
    '''
    this function is the main game.
    first the user is given the option to load or intilze a new game.
    when a new game is intilized or a game is loaded there is a main game loop.
    
    '''
    #prints text based intro screen
    print("*"*55)
    print("***"+" "*8+"WELCOME TO LUKA CONNECT FOUR!"+" "*8+"***")
    print("*"*55,"\n")
    print("Enter 'L' to load a game or Press the Enter key to play a new game.\n")
    #capitalizes intput 
    intial_choice = input()
    intial_choice = intial_choice.capitalize()
    
    if intial_choice == 'L':
        #the player chooses to load a game
        filename = input("please enter the file name: ")
        if loadGame(filename) == False:
            sys.exit("error no such file name exsits")
        game_dict = loadGame(filename)
        player1 = game_dict['player1']
        player2 = game_dict['player2']
    
    
    else:
        #player starts a new game 
        player1 = input("Player 1: ") 
        while player1 == "":
            print("Please enter a Non-empty Player name ")
            player1 = input("Player 1: ")
            
        player2 = input("player 2: ") 
        while player2 == "":
            print("Please enter a Non-empty Player name ")
            player2 = input("player 2: ")
        #capitalizes player names and makes a new game
        player1 = player1.capitalize()
        player2 = player2.capitalize()
        game_dict = newGame(player1,player2)
   
    
    #assigns the turn and board from the dic    
    turn = game_dict.get('who')
    board =game_dict.get('board')
    
    #checks which players are human
    if game_dict['player1'] == "C":
        is_human1 =False
    else:
        is_human1 =True
    if game_dict['player2'] == "C":
        is_human2 =False
    else:
        is_human2 =True
    
   #main game loop 
    while True:
        #player1 turn
        if turn ==1:
        
            printBoard(board)
            print("It is "+str(game_dict.get('player1'))+"'s turn")
            #checks for draw
            if getValidMoves(board) ==[]:
                print("The board is full, Its a draw!")
                break
            #computer turn
            elif is_human1==False:
                if computer_turn(board,1) == True:
                    game_has_been_won(board,player1,player2,turn)
                    break
            #human turn   
            else:
                if human_turn(board,1,game_dict) == True:
                        game_has_been_won(board,player1,player2,turn)
                        break   
            turn =2
            
        #player2 turn            
        if turn ==2:
            
            printBoard(board)
            print("It is "+str(game_dict.get('player2'))+"'s turn")
            #checks for draw
            if getValidMoves(board) ==[]:
                print("The board is full, Its a draw!")
                break
            #computer turn
            elif is_human2==False:
                if computer_turn(board,2) == True:
                    game_has_been_won(board,player1,player2,turn)
                    break
            #human turn    
            else:
                if human_turn(board,2,game_dict) == True:
                        game_has_been_won(board,player1,player2,turn)
                        break
            turn =1
    

def human_turn(board,turn,game):
    '''
    this is a helper function for play()
    it checks the move is valid and if the player wants to save the game.
    after a valid move is given it updates the board with the move and checks the win
    '''
    invalid_move = True
    #checks the inuputs until a vaild move is moad
    while invalid_move == True: 
        move = input("please enter a valid move: ")
        #player chooses to save the game
        if move == 'S':  
            filename = input("enter a filename ")
            if saveGame(game,filename) ==True:
                print("game has been saved ")
                continue
            else:
                print("the game failed to save")
                continue
        #player chooses makes a move
        else:
            try:
                move = int(move)-1
            except ValueError:
                print("valueError")
                continue
            if getValidMoves(board).count(move) !=1:
                continue
            invalid_move=False
    #makes the move
    board = makeMove(board,move,turn)
    return hasWon(board,turn)

def computer_turn(board,turn):
    '''
    this is a helper function for play
    when a its a computer players turn this function is called 
    and a move is suggested and made. 
    '''
    #suggests a move
    move = suggestMove2(board,turn) 
    #makes suggested move
    board = makeMove(board,move,turn)
    return hasWon(board,turn)

def game_has_been_won(board,player1,player2,turn):
    '''
    prints a winning message when the player wins a game
    '''
    players = [player1,player2]
    printBoard(board)
    print(players[turn-1]+" has won!")
    
    
def loadGame(filename):
    '''
    this function takes a fileaname input and opens a file with the name 'filename'
    it converts the txt file into the correct format and updates the game diconary by
    returning it
    '''
    #loads game.txt by default
    if filename == "":
        filename = "game.txt"
    #excepts filenotfound error
    try:    
        file = open(filename,'r')
    except FileNotFoundError:
        return False
    #converts from txt file format into dic format
    game = {}
    temp1=[]
    for lines in range(3):
        current_line = file.readline()
        current_line = current_line.rstrip()
        temp1.append(current_line)  
    try:
        game['player1'] = temp1[0]
        game['player2'] = temp1[1]
        game['who'] = int(temp1[2])
    except ValueError:
        return False
    temp2 = []
    for line in range(2,8):
        current_line = file.readline()
        current_line = current_line.rstrip()
        number = (current_line.split(','))
        for n in range(len(number)):
            number[n] = int(number[n])
        temp2.append(number)
    game['board'] = temp2
    #closes the flie
    file.close()
    return game

    
def saveGame(game,filename):
    '''
    this function takes a dictionary and filename as inputs and takes the information from
    the dictionary and converts it to the correct format to be written to a text file under
    the name filename
    '''
    #saves game.txt by default
    if filename == '':
        filename = 'game.txt'
    #saves the file as a .txt file    
    if filename[len(filename)-4:len(filename)] != '.txt':
        filename = filename+'.txt'
    #opens the file    
    file = open(filename,'w')
    #converts from the dic format into text file format
    file.write(game['player1']+'\n')
    file.write(game['player2']+'\n')
    file.write(str(game['who'])+'\n')
    copy_board = copy.deepcopy(game['board'])
    for i in range(6):
        for j in range(7):
            copy_board[i][j] = str(copy_board[i][j])
    copy_board = [''.join(x) for x in copy_board]
    for n in range(6):
        temp = list(copy_board[n])
        file.write(','.join(temp)+'\n')
    #closes the file
    file.close()
    return True 
   
def calculate_chunk_score(chunk,who):
    '''
    this function takes a chunk (list of 4 spaces on the board)
    and the player whos turn it is and cacluates the score based on 
    whos pieces are in the chunk.
    '''
    
    score = 0
    if who == 1:
        player = 1
        opponent = 2
    else:
        player = 2
        opponent = 1

    if chunk.count(player) == 4:#if the move results in 4 of your pieces 
        #in a chunk then this results in a win so this gives the highest score 
        score += 100
    elif chunk.count(player) == 2 and chunk.count(0) == 2:#gives incentive to make 2 in a row
        score += 3
    elif chunk.count(player) == 3 and chunk.count(0) == 1:#3 in a row
        score += 5
    if chunk.count(opponent) == 3 and chunk.count(0) == 1:#gives incentive to block the opponet
        score -= 15
    
    return score

def chunk_scores(board,who):
    '''
    this generates chunks of 4 spaces on the board in vertical horizontal
    and diagonal directions. once all possible chunks are generated as lists, 
    their scores are each calcuated and summed up to give the total score of the move 
    that is made.
    '''
    
    score = 0
    
    #center
    center_chunks = [board[i][3] for i in range(6)]
    center_score = center_chunks.count(who)
    score += center_score * 3

    #horizontal
    for p in range(row_len):
        for b in range(col_len-3):
            chunk = [board[p][b+i] for i in range(4)]
            score += calculate_chunk_score(chunk,who)
    
    #diagonals
    for p in range(row_len-3):
        for b in range(col_len-3):
            chunk = [board[p+i][b+i] for i in range(4)]
            score += calculate_chunk_score(chunk,who)
            
    for p in range(row_len-3):
        for b in range(col_len-3):
            chunk = [board[(p+3)-i][b+i] for i in range(4)]
            score += calculate_chunk_score(chunk,who)
    
    #Vertical
    for p in range(col_len):
        for b in range(row_len-3):
            chunk = [board[b+i][p] for i in range(4)]
            score += calculate_chunk_score(chunk,who)
    
    
    return score
            
def suggestMove2(board,who):
    '''
    this functinon is called when the computer is making a move.
    it takes the board and whos turn it is as inputs.
    first it gets a list a valid moves and then sets best_Move to  a random move. 
    it then makes all the valid moves on a deepcopy of the board
    one by one and cacluates the score of this move using the chunk_score function, 
    it then compares the new score of the current move and compares it to the 
    current top score which is initilzed as a large negative number.
    the move restsulting in the high score is the
    move that will be returned by the function.
    '''
    valid_moves = getValidMoves(board)#gets validmoves
    high_score = -175874875673
    best_move = random.choice(valid_moves)#chooses a random move
    
    for i in range(len(valid_moves)):
        copy3 = copy.deepcopy(board)#makes a deepcopy of the board
        copy3 = makeMove(copy3,valid_moves[i],who)
        score =  chunk_scores(copy3,who)#calculates the score
        
        if score > high_score:#compares the score
            high_score = score#updates high score
            best_move = valid_moves[i]#updates best move
    
    return best_move


    
      
if __name__ == '__main__' or __name__ == 'builtins':
    play()
 

  
 
 
 
 