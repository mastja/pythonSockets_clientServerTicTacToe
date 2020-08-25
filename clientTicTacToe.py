# Project 4 - Server and Client Chat Program - Client file
# Programmer - Jacob Mast
# Date 8/5/2020
# Description - Simple client-server program using python sockets. Program emulates a simple chat client. 
# source. 1 - https://www.binarytides.com/python-socket-programming-tutorial/
# source. 2 - https://realpython.com/python-sockets/#running-the-echo-client-and-server
# source. 3 - https://www.geeksforgeeks.org/socket-programming-python/#:~:text=One%20socket(node)%20listens%20on,real%20backbones%20behind%20web%20browsing.
# source. 4 - https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
# source. 5 - https://stackoverflow.com/questions/45936401/string-comparison-does-not-work-in-python
# source. 6 - https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874

import socket	#for sockets

#source for setting up the socket - https://www.geeksforgeeks.org/socket-programming-python/#:~:text=One%20socket(node)%20listens%20on,real%20backbones%20behind%20web%20browsing.
# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
  
# Define the port on which you want to connect 
port = 8888    
name = 'Client'            
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

#source for code and loop below: https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
#send name first, receive name from server
s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()

#print initial board and instructions
print '\n' + s_name + ' has joined the Tic Tac Toe game\nEnter "/q" to exit the game \n'

# source for tic tac toe game - https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)
            
def printBoard(board):
    print `board['7'] + '|' + board['8'] + '|' + board['9']`
    print '-+-+-+-'
    print `board['4'] + '|' + board['5'] + '|' + board['6']`
    print '-+-+-+-'
    print `board['1'] + '|' + board['2'] + '|' + board['3']`

#quit message from server, for use in if statement below
server_quit = 'Left the game!'

count = 0

turn = 'X'

print 'Here is a look at the board.  When playing, enter one of the\n'
print 'numbers in the board below to select the corresponding space.\n'
print `'7' + '|' + '8' + '|' + '9'`
print '-+-+-+-'
print `'4' + '|' + '5' + '|' + '6'`
print '-+-+-+-'
print `'1' + '|' + '2' + '|' + '3'`

#send and receive messages with the server in loop until a quit message is either sent or received
while True:
    print 'Waiting for Server to make a move...'
    message = s.recv(1024)
    message = message.decode()
    print "\n" + s_name + "'s Move"
    turn = 'X'
    if message == server_quit:
        print '\nServer Quit the Program'
        break
    move = message        
    if theBoard[move] == ' ':
        theBoard[move] = turn
        count += 1
    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
            printBoard(theBoard)
            print '\nGame Over.\n'  
            print  ' **** ' + s_name + ' won. ****'             
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
            printBoard(theBoard)
            print '\nGame Over.\n'  
            print  ' **** ' + s_name + ' won. ****'
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
            printBoard(theBoard)
            print '\nGame Over.\n'  
            print  ' **** ' + s_name + ' won. ****'
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
            printBoard(theBoard)
            print '\nGame Over.\n'  
            print  ' **** ' + s_name + ' won. ****'
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
            printBoard(theBoard)
            print '\nGame Over.\n'  
            print  ' **** ' + s_name + ' won. ****'
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
            printBoard(theBoard)
            print '\nGame Over.\n'  
            print  ' **** ' + s_name + ' won. ****'
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
            printBoard(theBoard)
            print '\nGame Over.\n'  
            print  ' **** ' + s_name + ' won. ****'
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
            printBoard(theBoard)
            print '\nGame Over.\n'  
            print  ' **** ' + s_name + ' won. ****'
            break 
    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:
        print '\nGame Over.\n'              
        print "It's a Tie!!"
        printBoard(theBoard)
        break
    printBoard(theBoard)
    # Client's turn
    print "It's your turn, " + name + '. You are O.\n'
    turn = 'O'
    while True:
        print 'Move to which place?'

        move = raw_input(str('Me : '))
        move = move.strip()	#source: https://stackoverflow.com/questions/45936401/string-comparison-does-not-work-in-python
        # if the client entered the quit key
        if move == '/q':
            move = 'Left the game!'
            s.send(move.encode())
            print '\nYou ended the game.'
            break
        # if it is a valid move
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
            print "Here's Your Move\n"
            printBoard(theBoard)
            break
        # it is not a valid move
        else:
            print 'That place is already filled.\n'
            printBoard(theBoard)

    if move == 'Left the game!':
        break

    # now check if Client won
    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
            print '\nGame Over.\n'  
            print  ' **** ' + name + ' won. ****'
            s.send(move.encode())   
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
            print '\nGame Over.\n'  
            print  ' **** ' + name + ' won. ****'
            s.send(move.encode())
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
            print '\nGame Over.\n'  
            print  ' **** ' + name + ' won. ****'
            s.send(move.encode())
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
            print '\nGame Over.\n'  
            print  ' **** ' + name + ' won. ****'
            s.send(move.encode())
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
            print '\nGame Over.\n'  
            print  ' **** ' + name + ' won. ****'
            s.send(move.encode())
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
            print '\nGame Over.\n'  
            print  ' **** ' + name + ' won. ****'
            s.send(move.encode())
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
            print '\nGame Over.\n'  
            print  ' **** ' + name + ' won. ****'
            s.send(move.encode())
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
            print '\nGame Over.\n'  
            print  ' **** ' + name + ' won. ****'
            s.send(move.encode())
            break
    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:
        print '\nGame Over.\n'
        print "It's a Tie!!"
        s.send(move.encode())
        break
    s.send(move.encode())

# close the connection 
s.close()
print 'program closing'