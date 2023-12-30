def main():
	path = {}
	total_steps = 0
	directions = ""
	with open("input.txt") as input:
		for i, row in enumerate(input):
			if i == 0:
				directions = row.strip()
				continue
			if i == 1:
				continue

			row = row.strip().split()
			element = row[0]
			left = row[2][1:4]
			right = row[3][:3]
			path[element] = (left, right)
	curr = "AAA"
	while True:
		if curr == "ZZZ":
			break

		for direction in directions:
			if direction == "L":
				curr = path[curr][0]
			elif direction == "R":
				curr = path[curr][1]
			total_steps += 1
	
	print(total_steps)
	return total_steps

main()