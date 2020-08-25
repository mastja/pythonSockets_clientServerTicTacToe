# Client-Server Tic Tac Toe Game using Socket Programming in Python 
# pythonSockets_clientServerTicTacToe

This program utilizes sockets to create a client-server chat tic tac toe game program in python.  The server makes the first move after the connection is established.  
Moves alternate between the client and the server.  Winning or tie-ing is determined by classic game rules for tic tac toe.
Client or Server may send the message, '/q', to quit the program.

Instructions to run program:
1)	Run serverTicTacToe.py
  a.	Open a terminal and run the server.py file using command:
    i.	run serverTicTacToe.py
2)	Run clientTicTacToe.py
  a.	Open another terminal and run the client.py file using command:
    i.	run clientTicTacToe.py
    
Note.01: Game does not handle input outside of expected range [1,9] & ‘/q’
Note.02:  Using Python 2.7
