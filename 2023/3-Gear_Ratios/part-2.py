from dataclasses import dataclass

@dataclass
class cell:
	content: str
	read: bool = False

def main():
	gear_ratio_sum = 0
	gear_locations: set[tuple[int]] = set()
	schematic: list[list[cell]] = []
	row, column = (0, 0)
	with open("input.txt", encoding="utf-8") as input:
		for content in input:
			column = 0
			r = [cell(content=".")]
			content = content.strip()
			for c in content:
				r.append(cell(content=c))
				if c == "*":
					gear_locations.add((row+1, column+1))
				column += 1
			r.append(cell(content="."))
			row += 1
			schematic.append(r)
	schematic.insert(0, [cell(content=".") for _ in range(column+2)])
	schematic.append([cell(content=".") for _ in range(column+2)])

	for gear in gear_locations:
		gear_ratios = []
		for x in range(-1, 2):
			for y in range(-1, 2):
				gear_ratio = 0
				coords = (gear[0] + x, gear[1] + y)
				if schematic[coords[0]][coords[1]].content.isdigit() and not schematic[coords[0]][coords[1]].read:
					gear_ratio = get_number(schematic[gear[0]+x], gear[1]+y)
				if gear_ratio != 0:
					gear_ratios.append(gear_ratio)
		if len(gear_ratios) == 2:
			gear_ratio_sum += gear_ratios[0] * gear_ratios[1]

	print(gear_ratio_sum)
	return gear_ratio_sum

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