sequence: dict[int: list[int]] = {}

def main():
	total = 0

	instructions = True
	# Only stores before because we only need to check this
	updates: list[list[int]] = []

	with open("input.txt") as input:
		for line in input:
			line = line.strip()
			if line == "":
				instructions = False
				continue
			if instructions:
				before, after = map(int, line.split(sep="|"))
				sequence[after] = sequence.get(after) or []
				sequence[after].append(before)
			if not instructions:
				update = list(map(int, line.split(sep=",")))
				updates.append(update)
	
	wrong_updates = []

	for update in updates:
		if correct_order(update):
			middle = update[len(update) // 2]
			total += middle
		else:
			wrong_updates.append(",".join(map(str, update))+"\n")
	
	with open("wrong.txt", mode="w") as wrong:
		wrong.writelines(wrong_updates)

	print(total)

	return 0

def correct_order(update: list[int]) -> bool:
	update_len = len(update)

	for i, page in enumerate(update):
		for p in update[i:]:
			if p in sequence[page]:
				return False
	
	return True

if __name__ == "__main__":
	main()