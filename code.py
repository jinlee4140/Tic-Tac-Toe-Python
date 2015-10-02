#Python Tic-Tac-Toe
import random
#The game board
board = [0, 1, 2,
		 		 3, 4, 5,
				 6, 7, 8]

def show():
	print board[0], '|',board[1], '|',board[2]
	print '-----------'
	print board[3], '|',board[4], '|',board[5]
	print '-----------'
	print board[6], '|',board[7], '|',board[8]

	while True:

		print "Select a spot."
		input = raw_input("> ")
		input = int(input)

		if board[input] != 'x' and board[input] != 'o':
			board[input] = 'x'

			finding = True

			while finding:
				random.seed() #gives a random generator
				opponent = random.rantint(0,8)

				if board[opponent] != 'o' and board[opponent]	!= 'x':
					board[opponent] = 'o'
					finding = False	



		else:
			print "The spot is taken! choose a different spot."


# show()

print random.seed()