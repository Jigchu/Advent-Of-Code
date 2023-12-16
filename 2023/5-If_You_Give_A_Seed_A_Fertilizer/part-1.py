def main():
	states: list[int] = []
	maps: list[int] = []
	map_num = 0

	with open("input.txt") as input:
		new_map = False
		for row in input:
			row = row.strip()
			if "seeds:" in row:
				states = list(map(int, row.split()[1:]))
				continue
			if "map" in row:
				maps.append([])
				new_map = True
				map_num += 1
				continue
			if row == "":
				new_map = False
				continue
			if new_map:
				row = list(map(int, row.split()))
				m = (row[0], (row[1], row[1] + row[2]))
				maps[map_num-1].append(m)
				continue

	for i in range(len(states)):
		for section in maps:
			for m in section:
				if states[i] in range(m[1][0], m[1][1]):
					states[i] = m[0] + (states[i] - m[1][0])
					break
	
	print(min(states))
	return min(states)
		
main()