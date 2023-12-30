def main():
	path = {}
	total_steps = 0
	directions = ""
	starts = []
	with open("input.txt") as input:
		for i, row in enumerate(input):
			if i == 0:
				directions = row.strip()
				continue
			if i == 1:
				continue
			
			row = row.strip().split()
			element = row[0]
			if element[2] == "A":
				starts.append(element)
			left = row[2][1:4]
			right = row[3][:3]
			path[element] = (left, right)

	steps_each = []
	for curr in starts:
		steps = 0
		while True:
			if curr[2] == "Z":
				break
			for direction in directions:
				if direction == "L":
					curr = path[curr][0]
				elif direction == "R":
					curr = path[curr][1]
				steps += 1
		steps_each.append(steps)

	total_steps = lcm(steps_each)
	print(total_steps)
	return total_steps

def p_factors(x):
	primes = {}
	while x > 1:
		for i in range(2, x + 1):
			if x % i == 0:
				primes[i] = 1 if primes.get(i) == None else primes[i] + 1
				x //= i
				break
	return primes

def lcm(nums: list[int]):
	exponents = {}
	lcm = 1
	for num in nums:
		for factor, exponent in p_factors(num).items():
			if exponents.get(factor) == None:
				exponents[factor] = exponent
				continue
			if exponents[factor] < exponent:
				exponents[factor] = exponent
	for factor, exponent in exponents.items():
		lcm *= factor**exponent
	return lcm

main()