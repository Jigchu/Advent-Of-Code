import math

def main():
	total = 0
	equations = []

	with open("input.txt") as input:
		for line in input:
			result, equation = line.strip().split(sep=":")
			result = int(result)
			equation = list(map(int, equation.strip().split()))
			equations.append((result, equation))
	
	for equation in equations:
		result = equation[0]
		values = equation[1]

		if brute_force(result, values):
			total += result

	print(total)

	return 0

def brute_force(result, values):
	num_values = len(values)
	num_operators = num_values - 1
	
	for i in range(2**num_operators):
		operators = bin(i)[2:].zfill(num_operators)
		total = values[0]
		for j, operator in enumerate(operators):
			if operator == "0":
				total += values[j+1]
			elif operator == "1":
				total *= values[j+1]
		if result == total:
			return True
	return False

if __name__ == "__main__":
	main()