def main():
	left = []
	right = []

	with open("input.txt") as input:
		for line in input:
			left_int, right_int = map(int, line.strip().split())
			left.append(left_int)
			right.append(right_int)

	left.sort()
	right.sort()
	list_len = len(left)
	
	total_distance = 0

	for i in range(list_len):
		total_distance += abs(left[i] - right[i])
	
	print(total_distance)

	return 0

if __name__ == "__main__":
	main()