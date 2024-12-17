wordsearch: list[list[str]] = []

def main():
	total = 0
	x_location = []

	with open("input.txt") as input:
		for y, line in enumerate(input):
			wordsearch.append(list(line.strip()))
			for x, char in enumerate(line):
				if char == "X":
					x_location.append((x, y))
	print(*x_location)
	for location in x_location:
		x, y = location
		for y_offset in range(-1, 2):
			for x_offset in range(-1, 2):
				new_x = x + x_offset
				new_y = y + y_offset
				if new_x < 0 or new_y < 0:
					continue
				try:
					letter = wordsearch[new_y][new_x]
				except IndexError:
					continue
				if letter == "M":
					word = search_for_XMAS((x, y), get_direction(x_offset, y_offset))
					if word == "XMAS":
						total += 1

	print(total)

	return 0

def get_direction(x_offset, y_offset):
	direction = ""
	if y_offset == -1:
		direction += "N"
	if y_offset == 1:
		direction += "S"
	if x_offset == -1:
		direction += "W"
	if x_offset == 1:
		direction += "E"
	
	return direction

def get_offset(direction):
	x_offset = 0
	y_offset = 0
	for letter in direction:
		if letter == "N":
			y_offset = -1
		if letter == "S":
			y_offset = 1
		if letter == "W":
			x_offset = -1
		if letter == "E":
			x_offset = 1
	
	return x_offset, y_offset

# His only job in life is to search for the word XMAS in a certain direction
def search_for_XMAS(start_location, direction):
	x_offset, y_offset = get_offset(direction)
	x, y = start_location
	word = wordsearch[y][x]
	for _ in range(3):
		x += x_offset
		y += y_offset
		if x < 0 or y < 0:
			break
		try:
			letter = wordsearch[y][x]
		except IndexError:
			break
		word = word + letter

	return word

if __name__ == "__main__":
	main()