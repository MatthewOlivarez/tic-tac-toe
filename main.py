def printBoard(squares):
	for i in range(3):
		if i == 2:
			print(' ', end='')
		else:
			print('_', end='')
		for j in range(3):
			if (i == 0 or i == 1) and j != 2:
				print(squares[i][j] + '_|_', end='')
			elif (i == 0 or i == 1) and j == 2:
				print(squares[i][j] + '_', end='')
			else:
				if i == 2 and (j == 0 or j == 1):
					print(squares[i][j] + ' | ', end='')
				else:
					print(squares[i][j] + ' ', end='')
		print('')


def gameLogic(arr, let):
	sameSpot = True

	while sameSpot:
		num = int(input('Type 1-9 to place a piece on the board: '))
		switcher = {
			1: [0,0],
			2: [0,1],
			3: [0,2],
			4: [1,0],
			5: [1,1],
			6: [1,2],
			7: [2,0],
			8: [2,1],
			9: [2,2]
		}
		if arr[switcher[num][0]][switcher[num][1]] == ' ':
			arr[switcher[num][0]][switcher[num][1]] = let
			sameSpot = False
		else:
			print('That spot is taken. Try again!')
		

def checkWinner():
	if ((arr[0][0] == let and arr[0][1] == let and arr[0][2] == let) or
	   (arr[1][0] == let and arr[1][1] == let and arr[1][2] == let) or
	   (arr[2][0] == let and arr[2][1] == let and arr[2][2] == let) or
	   (arr[0][0] == let and arr[1][0] == let and arr[2][0] == let) or
	   (arr[0][1] == let and arr[1][1] == let and arr[2][1] == let) or
	   (arr[0][2] == let and arr[1][2] == let and arr[2][2] == let) or
	   (arr[0][0] == let and arr[1][1] == let and arr[2][2] == let) or
	   (arr[0][2] == let and arr[1][1] == let and arr[2][0] == let)):
	   return False
	else:
		 return True



board = []
noWinner = True
count = 0
player = 'X'
num = 0

for i in range(3):
	col = []
	for j in range(3):
		col.append(' ')
	board.append(col)

print('Let\'s play tic-tac-toc! X goes first.')

while noWinner and count < 9:
	printBoard(board)
	gameLogic(board, player)
	noWinner = checkWinner(board, player)
	count += 1
	if player == 'X':
		if noWinner and count < 9:
			player = 'O'
	else:
		if noWinner and count < 9:
			player = 'X'

print('The winner is ' + player)






