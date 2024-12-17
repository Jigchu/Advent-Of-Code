def main():
	left = []
	right_freq = {}
	similarity = 0

	with open("input.txt") as input:
		for line in input:
			left_int, right_int = map(int, line.strip().split())
			left.append(left_int)
			try:
				right_freq[right_int] += 1
			except KeyError:
				right_freq[right_int] = 1

	for i in left:
		try:
			similarity += i * right_freq[i]
		except KeyError:
			pass

	print(similarity)

	return 0

if __name__ == "__main__":
	main()