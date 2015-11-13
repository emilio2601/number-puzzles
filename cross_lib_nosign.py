import itertools as it

def generate_all_boards(elements):
	row_perms = it.permutations(elements)
	boards = []

	for i in it.permutations(row_perms, 4):
		if is_valid_board(i):
			boards.append(i)
	return boards

def test_board(board, row_goals, col_goals, get_solutions=False):
	if not get_solutions:
		sign_combinations = ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]
		if test_rows(board, sign_combinations, row_goals):
			if test_cols(board, sign_combinations, col_goals):
				return True
		return False
	if get_solutions:
		sign_combinations = ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]
		if test_rows(board, sign_combinations, row_goals):
			if test_cols(board, sign_combinations, col_goals):
				return [test_rows(board, sign_combinations, row_goals, get_solutions=True), test_cols(board, sign_combinations, col_goals, get_solutions=True)]
		return False


def print_solution(solution):
	print()
	print("Solution: ")
	print("Rows: ")
	for row in solution[0]:
		print(row)
	print("Columns: ")
	for col in solution[1]:
		print(col)

def test_rows(board, signs, goals, get_solutions=False):
	if not get_solutions:
		for index, row in enumerate(board):
			if not test_line(row, signs, goals[index]): 
				return False
		return True
	if get_solutions:
		solutions = []
		for index, row in enumerate(board):
			if test_line(row, signs, goals[index]):
				solutions.append(test_line(row,signs,goals[index],get_solutions=True))
		return solutions


def test_line(line, signs, goal, get_solutions=False):
	#line = [5, 6, 7, 8]
	#signs = ["+-*", "-*+"]
	#goal = 44
	if not get_solutions:
		for sign in signs:
			expr = "{0}{1}{2}{3}{4}{5}{6}".format(line[0], sign[0], line[1], sign[1], line[2], sign[2], line[3])
			if eval_dhp(expr) == goal:
				return True
		return False
	if get_solutions:
		for sign in signs:
			expr = "{0}{1}{2}{3}{4}{5}{6}".format(line[0], sign[0], line[1], sign[1], line[2], sign[2], line[3])
			if eval_dhp(expr) == goal:
				return expr
		return False
	

def test_cols(board, signs, goals, get_solutions=False):
	if not get_solutions:
		for index, col in enumerate(list(zip(*board))):
			if not test_line(col, signs, goals[index]): 
				return False
		return True
	if get_solutions:
		solutions = []
		for index, col in enumerate(list(zip(*board))):
			if test_line(col, signs, goals[index]):
				solutions.append(test_line(col, signs, goals[index], get_solutions=True))
		return solutions

def is_valid_board(board):
	for index_r, row in enumerate(board):
		for index_e, element in enumerate(row): #Para cada elemento con coordenadas board[index_r, index_e]
			if row.count(element) == 1:
				if list(zip(*board))[index_e].count(element) == 1:
					continue
				else:
					return False
			else:
				return False
	return True



def eval_dhp(expr):
	expr_array = list(expr)
	result = 0
	next_token = "NUMBER"
	next_op = "+"
	for token in expr_array:
		if token == " ": continue
		if next_token == "NUMBER":
			if next_op == "+":
				result += int(token)
			if next_op == "*":
				result *= int(token)
			if next_op == "-":
				result -= int(token)
			next_token = "SIGN"
		if next_token == "SIGN":
			next_op = token
			next_token = "NUMBER"
	return result

