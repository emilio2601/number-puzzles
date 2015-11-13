import pprint
import itertools as it

def solve_row(problem_str, result, num_range):
	answers = []
	for perm in it.permutations(num_range):
		result_str = replace(problem_str, perm, "N")
		answer = eval_dhp(result_str)
		if answer == result:
			answers.append(perm)
	return answers

def replace(string, replacements, str_to_replace):
	for rp in replacements:
		rp = str(rp)
		string = string.replace(str_to_replace, rp, 1)
	return string

def solve_all(array):
	solutions = []
	for i in array:
		ans_array = solve_row(i[0], i[1], [5,6,7,8])
		solutions.append(ans_array)
	return solutions

def form_matrix(solution_grid):
	columns = []
	for col in solution_grid:
		columns.append(list_intersection(list(col)))
	matrix = [[], [], [], []]
	col1 = columns[0]
	col2 = columns[1]
	col3 = columns[2]
	col4 = columns[3]
	matrix[0] = [col1[0], col2[0], col3[0], col4[0]]
	matrix[1] = [col1[1], col2[1], col3[1], col4[1]]
	matrix[2] = [col1[2], col2[2], col3[2], col4[2]]
	matrix[3] = [col1[3], col2[3], col3[3], col4[3]]
	return matrix

def list_intersection(array):
	result = array[0] # 5 6 7 8
	for index, alt in enumerate(array):
		if index == 0: pass
		else:
			result = compare(result, alt)
	return result

def compare(lista, listb):
	result = []
	for a, b in zip(lista,listb):
			if a == b:
				result.append(a)
			else:
				result.append(None)
	return result

def complete_matrix(matrix,num_range=[5,6,7,8]):
	iterations = 1
	while not check_finish(matrix):
		matrix = fill_all_with_missing(matrix, num_range)
		matrix = fill_by_row_elimination(matrix, num_range)
		print("Lol")
		iterations += 1
		if iterations == 100: break
	return matrix

def fill_by_row_elimination(matrix, num_range):
	col1 = [ row[0] for row in matrix ]
	col2 = [ row[1] for row in matrix ]
	col3 = [ row[2] for row in matrix ]
	col4 = [ row[3] for row in matrix ]
	col = [col1, col2, col3, col4]

	values = set(num_range)

	for index_r, row in enumerate(matrix):
		if row.count(None) > 0: #Entonces hay valores que tenemos que revisar en la fila
			for index, element in enumerate(row):
				if element == None: #Revisemos este elemento
					row_missing = values.difference(set(row))
					col_missing = values.difference(set(col[index]))
					common = row_missing.intersection(col_missing)
					if len(common) == 1:
						matrix[index_r][index] = common.pop()
	return matrix

def check_finish(matrix):
	for row in matrix:
		for element in row:
			if element == None:
				return False
	return True

def fill_all_with_missing(matrix, num_range):
	col1 = [ row[0] for row in matrix ]
	col2 = [ row[1] for row in matrix ]
	col3 = [ row[2] for row in matrix ]
	col4 = [ row[3] for row in matrix ]

	if col1.count(None) == 1:
		col1 = fill_in(col1)
	if col2.count(None) == 1:
		col2 = fill_in(col2)
	if col3.count(None) == 1:
		col3 = fill_in(col3)
	if col4.count(None) == 1:
		col4 = fill_in(col4)

	matrix[0] = [col1[0], col2[0], col3[0], col4[0]]
	matrix[1] = [col1[1], col2[1], col3[1], col4[1]]
	matrix[2] = [col1[2], col2[2], col3[2], col4[2]]
	matrix[3] = [col1[3], col2[3], col3[3], col4[3]]

	for index, row in enumerate(matrix):
		if row.count(None) == 1:
			matrix[index] = fill_in(row, num_range=num_range)
	return matrix

def fill_in(row, num_range=[5,6,7,8]):
	reference = set(num_range)
	new = set(row)
	missing_val = reference.difference(new).pop()
	row = list_replace(row, None, missing_val)
	return row
	
def list_replace(list, val_search, val_substitute):
	for index, element in enumerate(list):
		if element == val_search:
			list[index] = val_substitute
	return list

def sign_test(full_matrix, results):
	answers = []
	sign_combinations = ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]
	for index, row in enumerate(full_matrix):
		for comb in sign_combinations:
			if test_signs(row, comb, results[index]):
				answers.append(comb)

	return answers

def test_signs(numbers, signs, goal):
	eval_str = "{} {} {} {} {} {} {}".format(numbers[0], signs[0], numbers[1], signs[1], numbers[2], signs[2], numbers[3])
	if eval_dhp(eval_str) == goal: return True
	else: return False

def print_final(matrix, signs, right_results):
	for index, row in enumerate(matrix):
		print("{} {} {} {} {} {} {} = {}".format(matrix[index][0], signs[index][0], matrix[index][1], signs[index][1], matrix[index][2], signs[index][2],  matrix[index][3], right_results[index]))

def eval_dhp(expr):
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

