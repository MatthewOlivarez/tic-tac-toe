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

squares = []
noWinner = True
count = 0

for i in range(3):
	col = []
	for j in range(3):
		col.append('X')


for i in range(3):
	if i == 2:
		print(' ', end='')
	else:
		print('_', end='')
	for j in range(1):
		if i == 0 or i == 1:
			print(' _|_ _|_ _', end='')
		else:
			print('  |   |   ', end='')
	print('')


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