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
		# The text is here to keep ADHD brains happy while the computer brute forces
		print(f"Done with {result}")

	print(total)

	return 0

def ternary(n):
    size = math.ceil(math.log(max(1,n),3))
    return "".join(map(str, [place
        for i in range(size,-1,-1)
        if (place := n//3**i%3) or i<size])) or "0"

def brute_force(result, values):
	num_values = len(values)
	num_operators = num_values - 1
	
	for i in range(3**num_operators):
		operators = ternary(i).zfill(num_operators)
		total = values[0]
		for j, operator in enumerate(operators):
			if operator == "0":
				total += values[j+1]
			elif operator == "1":
				total *= values[j+1]
			elif operator == "2":
				total = int(str(total) + str(values[j+1]))
		if result == total:
			return True
	return False

if __name__ == "__main__":
	main()