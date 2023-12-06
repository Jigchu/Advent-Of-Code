def main():
	total = 0
	with open("input.txt") as input:
		for case in input:
			case = list(case.strip())
			number = 0
			for i in range(2):
				place = 10 if i == 0 else 1
				for c in case:
					if c.isnumeric():
						number += int(c) * place
						break
				case.reverse()
			total += number
	print(total)
	return total

main()