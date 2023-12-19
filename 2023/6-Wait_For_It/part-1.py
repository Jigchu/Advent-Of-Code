def main():
	product_of_error = 1
	times: list[int] = []
	distances: list[int] = []

	with open("input.txt") as input:
		for row in input:
			row = row.strip()
			if "Time:" in row:
				row = list(map(int, row.split()[1:]))
				times = row
			elif "Distance:" in row:
				row = list(map(int, row.split()[1:]))
				distances = row
	
	total_races = len(times)
	
	for i in range(total_races):
		possibilities = 0
		time = times[i]
		distance = distances[i]
		for j in range(1, time):
			actual_distance = (time - j) * j
			if actual_distance > distance:
				possibilities += 1
		product_of_error *= possibilities

	print(product_of_error)
	return product_of_error

main()