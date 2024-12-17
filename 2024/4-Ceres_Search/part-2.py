wordsearch: list[list[str]] = []

def main():
	total = 0
	a_locations = []
	with open("input.txt") as input:
		for y, line in enumerate(input):
			wordsearch.append(list(line.strip()))
			for x, char in enumerate(line):
				if char == "A":
					a_locations.append((x, y))
	
	for location in a_locations:
		if check_for_X_shaped_MAS(location) == True:
			total += 1

	print(total)

	return 0

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

# Aptly named function
def check_for_X_shaped_MAS(location) -> bool:
	x, y = location
	accepted = ["MS", "SM"]
	offsets = {
		"NW": "",
		"NE": "",
		"SW": "",
		"SE": "",
	}

	for offset in offsets:
		x_offset, y_offset = get_offset(offset)
		new_x = x + x_offset
		new_y = y + y_offset
		if new_x < 0 or new_y < 0:
			return False
		try:
			offsets[offset] = wordsearch[new_y][new_x]
		except IndexError:
			return False

	top_left_diagonal = offsets["NW"] + offsets["SE"]
	top_right_diagonal = offsets["NE"] + offsets["SW"]

	if top_left_diagonal in accepted and top_right_diagonal in accepted:
		return True
	
	return False

if __name__ == "__main__":
	main()