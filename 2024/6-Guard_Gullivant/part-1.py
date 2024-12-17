lab_map: list[list[str]] = []

def main():
	guard_location = []
	total = 0
	guard_direction = "N"
	# x shows y coords because I want to look up the other coord
	locations: dict[str, list[list[int]]] = {
		'x': [],
		'y': [],
	}

	with open("input.txt") as input:
		for line in input:
			lab_map.append(list(line.strip()))

	locations['x'] = [[] for _ in range(len(lab_map[0]))]
	locations['y'] = [[] for _ in range(len(lab_map))]
	map_dimensions = (len(lab_map[0]), len(lab_map))

	for y, row in enumerate(lab_map):
		for x, c in enumerate(row):
			if c == "#":
				locations['x'][x].append(y)
				locations['y'][y].append(x)
			if c == "^":
				guard_location = [x, y]

	while True:
		if guard_direction == "N":
			obstacles = locations["x"][guard_location[0]]
			obstacles = [i for i in obstacles if i < guard_location[1]]
			if len(obstacles) == 0:
				colour(guard_location, (guard_location[0], map_dimensions[1]), guard_direction)
				break
			colour(guard_location, (guard_location[0], max(obstacles)), guard_direction)
			guard_location[1] = max(obstacles) + 1
			guard_direction = "E"
		elif guard_direction == "S":
			obstacles = locations["x"][guard_location[0]]
			obstacles = [i for i in obstacles if i > guard_location[1]]
			if len(obstacles) == 0:
				colour(guard_location, (guard_location[0], map_dimensions[1]), guard_direction)
				break
			colour(guard_location, (guard_location[0], min(obstacles)), guard_direction)
			guard_location[1] = min(obstacles) - 1
			guard_direction = "W"
		elif guard_direction == "W":
			obstacles = locations["y"][guard_location[1]]
			obstacles = [i for i in obstacles if i < guard_location[0]]
			if len(obstacles) == 0:
				colour(guard_location, (guard_location[0], map_dimensions[1]), guard_direction)
				break
			colour(guard_location, (max(obstacles), guard_location[1]), guard_direction)
			guard_location[0] = max(obstacles) + 1
			guard_direction = "N"
		elif guard_direction == "E":
			obstacles = locations["y"][guard_location[1]]
			obstacles = [i for i in obstacles if i > guard_location[0]]
			if len(obstacles) == 0:
				colour(guard_location, (map_dimensions[0], guard_location[1]), guard_direction)
				break
			colour(guard_location, (min(obstacles), guard_location[1]), guard_direction)
			guard_location[0] = min(obstacles) - 1
			guard_direction = "S"

	for r in lab_map:
		for c in r:
			if c == "$":
				total += 1

	print(total)

	return 0

def get_offset(direction):
	if direction == "N":
		return -1
	if direction == "S":
		return 1
	if direction == "W":
		return -1
	if direction == "E":
		return 1

# End is not inclusive because its more convenient
def colour(start, end, direction):
	x, y = start
	end_x, end_y = end
	if direction in ["N", "S"]:
		offset = get_offset(direction)
		while y != end_y:
			lab_map[x][y] = "$"
			y += offset
	elif direction in ["W", "E"]:
		offset = get_offset(direction)
		while x != end_x:
			lab_map[x][y] = "$"
			x += offset

if __name__ == "__main__":
	main()