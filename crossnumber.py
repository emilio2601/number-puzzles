from cross_lib import *

if __name__ == '__main__':
	columns = [("N-N+N*N", 49), ("N-N*N+N", 15), ("N+N*N-N",85), ("N+N-N*N",24)]
	right_results = [45, 15, 48, 69]
	solutions = solve_all(columns)
	safe_matrix = form_matrix(solutions)
	final_matrix = complete_matrix(safe_matrix)
	signs = sign_test(final_matrix, right_results)
	print_final(final_matrix, signs, right_results)
	