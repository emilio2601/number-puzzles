import itertools as it

def generate_all_boards(elements):
	row_perms = it.permutations(elements)
	boards = []

	for i in it.permutations(row_perms, 4):
		if is_valid_board(i):
			boards.append(i)
	return boards




def test_board(board, row_goals, col_goals):
	sign_combinations = ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]

	if test_rows(board, sign_combinations, row_goals):
		print("Lol")
		if test_cols(board, sign_combinations, col_goals):
			return True

def test_rows(board, signs, goals):
	for index, row in enumerate(board):
		for comb in signs:
			string = "{0}{1}{2}{3}{4}{5}{6}".format(row[0], comb[0], row[1], comb[1], row[2], comb[2], row[3])
			if eval_dhp(string) == goals[index]: 
	return True

def test_line(line, signs, goal):
	

def test_cols(board, signs, goals):
	for index, col in enumerate(list(zip(*board))):
		for comb in signs:
			string = "{0}{1}{2}{3}{4}{5}{6}".format(col[0], comb[0], col[1], comb[1], col[2], comb[2], col[3])
			if eval_dhp(string) == goals[index]:
	return True

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

