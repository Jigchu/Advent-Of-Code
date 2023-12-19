def main():
	possibilities = 0
	times: list[int] = []
	distances: list[int] = []

	with open("input.txt") as input:
		for row in input:
			row = row.strip()
			if "Time:" in row:
				row = "".join(row.split()[1:])
				time = int(row)
			elif "Distance:" in row:
				row = "".join(row.split()[1:])
				distance = int(row)

	for j in range(1, time):
		actual_distance = (time - j) * j
		if actual_distance > distance:
			possibilities += 1

	print(possibilities)
	return possibilities

main()