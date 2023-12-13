from dataclasses import dataclass

@dataclass
class cell:
	content: str
	read: bool = False

def main():
	part_number_sum = 0
	symbol_locations: set[tuple[int]] = set()
	schematic: list[list[cell]] = []
	row, column = (0, 0)
	with open("input.txt", encoding="utf-8") as input:
		for content in input:
			column = 0
			r = [cell(content=".")]
			content = content.strip()
			for c in content:
				r.append(cell(content=c))
				if not c.isalnum() and c != ".":
					symbol_locations.add((row+1, column+1))
				column += 1
			r.append(cell(content="."))
			row += 1
			schematic.append(r)
	schematic.insert(0, [cell(content=".") for _ in range(column+2)])
	schematic.append([cell(content=".") for _ in range(column+2)])

	for location in symbol_locations:
		for x in range(-1, 2):
			for y in range(-1, 2):
				coords = (location[0] + x, location[1] + y)
				part_num = 0
				if schematic[coords[0]][coords[1]].content.isdigit() and not schematic[coords[0]][coords[1]].read:
					part_num = get_number(schematic[location[0]+x], location[1]+y)
					with open("output.txt", mode="a") as f:
						f.write(f"{part_num}\n")
				part_number_sum += part_num

	print(part_number_sum)
	return part_number_sum

def get_number(row, location):
	number = ""
	left: list[cell] = row[:location]
	left.reverse()
	right: list[cell] = row[location:]
	for c in left:
		if c.content.isdigit():
			number = c.content + number
			c.read = True
		else:
			break
	for c in right:
		if c.content.isdigit():
			number += c.content
			c.read = True
		else:
			break
	
	return 0 if number == "" else int(number)


main()