from cross_lib_nosign import *
import pprint

if __name__ == '__main__':
	column_goals = [25, 15, 61, 65]
	row_goals = [5, 21, 17, 77]

	boards = generate_all_boards([1,2,3,4])

	for board in boards:
		if test_board(board, row_goals, column_goals):
			print("Succeeded with board: {}".format(board))

