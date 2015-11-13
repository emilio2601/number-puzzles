from cross_lib_nosign import *
import time
import pprint
import time
if __name__ == '__main__':
	column_goals = [49,15,85,24]
	row_goals = [45,15,48,69]
	options = [5,6,7,8]

	start = time.time()
	print("Generating all possible boards for numbers {}".format(options))

	boards = generate_all_boards(options)
	time_taken = time.time() - start
	print("{} boards generated in {} seconds".format(len(boards), round(time_taken,5)))

	start_test = time.time()
	for index, board in enumerate(boards):
		if test_board(board, row_goals, column_goals):
			print("Succeeded with board {}".format(index+1))
			solution = test_board(board, row_goals, column_goals, get_solutions=True)
			break

	test_time = time.time() - start_test
	print("Test time: {} seconds".format(round(test_time,5)))
	try:
		print_solution(solution)
	except:
		print("No solution found")
	final_time = time.time() - start
	print("Total time: {} seconds".format(round(final_time,5)))

