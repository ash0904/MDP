import copy
x=19.0
rsa= -1*x/20.0
delta = -1*rsa
gamma = 1.0

def display(board):
	for i in range(4):
		print
		for j in range(4):
			print "",
			if type(board[i][j]) is float:
				print ("%.2f" %board[i][j]),
			else:
				print board[i][j],
		print
	print

board		   = [[0.0 for i in range(4) ] for j in range(5)]
board[0][0]	   = 'w'
board[0][1]	   = 'w'
board[0][2]	   =  x
board[0][3]	   = 'w'
board[2][1]	   = -1*x
board[2][2]	   = 'w'
states         = [(1,0),(1,1),(1,2),(1,3),(2,0),(2,3),(3,0),(3,1),(3,2),(3,3)]
possibleStates = [(0,2),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,3),(3,0),(3,1),(3,2),(3,3)]
# direc = ['n','s','w','e']
def check_north(move):
	v1 = (move[0]-1,move[1])
	v2 = (move[0],move[1]-1)
	v3 = (move[0],move[1]+1)
	move = (4,0)
	if v1 not in possibleStates:
		v1 = move
	if v2 not in possibleStates:
		v2 = move
	if v3 not in possibleStates:
		v3 = move
	return v1,v2,v3

def check_south(move):
	v1 = (move[0]+1,move[1])
	v2 = (move[0],move[1]-1)
	v3 = (move[0],move[1]+1)
	move = (4,0)
	if v1 not in possibleStates:
		v1 = move
	if v2 not in possibleStates:
		v2 = move
	if v3 not in possibleStates:
		v3 = move
	return v1,v2,v3

def check_east(move):
	v1 = (move[0],move[1]+1)
	v2 = (move[0]+1,move[1])
	v3 = (move[0]-1,move[1])
	move = (4,0)
	if v1 not in possibleStates:
		v1 = move
	if v2 not in possibleStates:
		v2 = move
	if v3 not in possibleStates:
		v3 = move
	return v1,v2,v3

def check_west(move):
	v1 = (move[0],move[1]-1)
	v2 = (move[0]-1,move[1])
	v3 = (move[0]+1,move[1])
	move = (4,0)
	if v1 not in possibleStates:
		v1 = move
	if v2 not in possibleStates:
		v2 = move
	if v3 not in possibleStates:
		v3 = move
	return v1,v2,v3
ite = 0
maxdif = 100000000
print "delta:	 ",delta
while maxdif >= delta:
	print "<<<<<<<<<<<<<<<<<Board after ",ite," iterations>>>>>>>>>>>>>>>>"
	display(board)
	ite+=1
	temp_board = copy.deepcopy(board)
	for move in states:

		mn1,mn2,mn3 = check_north(move)
		no = 0.8*board[mn1[0]][mn1[1]] + 0.1*board[mn2[0]][mn2[1]] + 0.1*board[mn3[0]][mn3[1]]

		mn1,mn2,mn3 = check_south(move)
		so = 0.8*board[mn1[0]][mn1[1]] + 0.1*board[mn2[0]][mn2[1]] + 0.1*board[mn3[0]][mn3[1]]

		mn1,mn2,mn3 = check_east(move)
		ea = 0.8*board[mn1[0]][mn1[1]] + 0.1*board[mn2[0]][mn2[1]] + 0.1*board[mn3[0]][mn3[1]]

		mn1,mn2,mn3 = check_west(move)
		we = 0.8*board[mn1[0]][mn1[1]] + 0.1*board[mn2[0]][mn2[1]] + 0.1*board[mn3[0]][mn3[1]]

		maxval = max(no,so,ea,we)
		temp_board[move[0]][move[1]] = maxval + rsa
		# print "move:",move,"maxval",maxval+rsa,"no",no+rsa,"so",so+rsa,"ea",ea+rsa,"we",we+rsa

	maxdif = 0
	for i in range(4):
		for j in range(4):
			if board[i][j]!='w':
				maxdif = max(maxdif,temp_board[i][j]-board[i][j])
	board = copy.deepcopy(temp_board)
print "final board"
print "no of iterations= ",ite
print "<<<<<<<<<<<<<<<<<Board after ",ite," iterations>>>>>>>>>>>>>>>>"
display(board)
