import re

def main():
	total = 0
	with open("input.txt") as input:
		for case in input:
			case = text_to_int(case)
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

def text_to_int(text: str):
	digits = {
		"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", 
		"six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e",
	}
	
	for key, item in digits.items():
		text = re.sub(fr"{key}", fr"{item}", fr"{text}")
	
	return text

main()