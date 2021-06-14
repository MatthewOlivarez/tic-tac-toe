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


def checkWinner():
	if ((arr[0][0] == let and arr[0][1] == let and arr[0][2] == let) or
	   (arr[0][0] == let and arr[0][1] == let and arr[0][2] == let) or
	   (arr[0][0] == let and arr[0][1] == let and arr[0][2] == let) or
	   (arr[0][0] == let and arr[0][1] == let and arr[0][2] == let) or
	   (arr[0][0] == let and arr[0][1] == let and arr[0][2] == let) or
	   (arr[0][0] == let and arr[0][1] == let and arr[0][2] == let) or
	   (arr[0][0] == let and arr[0][1] == let and arr[0][2] == let) or
	   (arr[0][0] == let and arr[0][1] == let and arr[0][2] == let)):
	   return False
	else:
		return True



board = []
noWinner = True
count = 0

for i in range(3):
	col = []
	for j in range(3):
		col.append('X')
	board.append(col)


printBoard(board)


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