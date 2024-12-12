def main():
	farthest_steps = 0
	
	maze = []
	start_pos = (0, 0)
	with open("input.txt", "r") as input:
		for row_num, row in enumerate(input):
			row = list(row.strip())
			maze.append(row)
			try:
				start_index = row.index("S")
			except ValueError:
				start_index = -1
			if start_index != -1:
				start_pos = (row_num, start_index)
	
	offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
	col_len = len(maze)
	row_len = len(maze[0])
	if start_pos[0] == 0:
		offsets.remove((-1, 0))
	elif start_pos[0] == col_len - 1:
		offsets.remove(1, 0)
	if start_pos[1] == 0:
		offsets.remove((0, -1))
	elif start_pos[1] == row_len - 1:
		offsets.remove((0, 1))

	possible_start = ["|", "-", "J", "F", "L", "7"] 
	for offset in offsets:
		for possibility in possible_start:
			next_pos = (start_pos[0]+offset[0], start_pos[1]+offset[1])
			rev_offset = (offset[0]*-1, offset[1]*-1)
			if not valid_pos(maze, next_pos, possibility, rev_offset) and not naive_valid_pos(maze, next_pos, offset):
				try:
					possible_start.remove(possibility)
				except ValueError:
					pass

	maze[start_pos[0]][start_pos[1]] = possible_start[0]

	next_positions = [start_pos]
	prev = (-1, -1)
	while True:
		curr = next_positions.pop()
		print(curr)
		if curr == start_pos and farthest_steps != 0:
			break
		next_positions.extend(next_valid_pipes(maze, curr, prev))
		prev = curr
		farthest_steps += 1

	farthest_steps //= 2
	print(farthest_steps)

	return farthest_steps

def next_valid_pipes(graph, curr, prev):
	next_valid = []
	curr_pipe = graph[curr[0]][curr[1]]
	offsets = []
	
	match curr_pipe:
		case "|":
			offsets = [(-1, 0), (1, 0)]
		case "-":
			offsets = [(0, -1), (0, 1)]
		case "L":
			offsets = [(-1, 0), (0, 1)]
		case "J":
			offsets = [(-1, 0), (0, -1)]
		case "F":
			offsets = [(1, 0), (0, 1)]
		case "7":
			offsets = [(1, 0), (0, -1)]

	col_len = len(graph)
	row_len = len(graph[0])
	if curr[0] == 0:
		try:
			offsets.remove((-1, 0))
		except ValueError:
			pass
	elif curr[0] == col_len - 1:
		try:
			offsets.remove((1, 0))
		except ValueError:
			pass
	if curr[1] == 0:
		try:
			offsets.remove((0, -1))
		except ValueError:
			pass
	elif curr[1] == row_len - 1:
		try:
			offsets.remove((0, 1))
		except ValueError:
			pass

	for offset in offsets:
		next_pos = (curr[0]+offset[0], curr[1]+offset[1])
		if next_pos == prev:
			continue
		next_valid.append(next_pos)

	return next_valid

def valid_pos(graph, curr, next_pipe, offset):
	curr_pipe = graph[curr[0]][curr[1]]

	if next_pipe == "." or curr_pipe == ".":
		return True

	match curr_pipe:
		case "|":
			if offset[1] == 0:
				match next_pipe:
					case "|":
						return True
					case "7", "F":
						if offset[0] == -1: return True
					case "L", "J":
						if offset[0] == 1: return True
		case "-":
			if offset[0] == 0:
				match next_pipe:
					case "-":
						return True
					case "L", "F":
						if offset[1] == -1: return True
					case "J", "7":
						if offset[1] == 1: return True
		case "J":
			if offset[0] == -1:
				if next_pipe in ["F", "7", "|"]: return True
			if offset[1] == -1:
				if next_pipe in ["L", "-"]: return True
		case "L":
			if offset[0] == -1:
				if next_pipe in ["F", "7", "|"]: return True
			if offset[1] == 1:
				if next_pipe in ["J", "-"]: return True
		case "F":
			if offset[0] == 1:
				if next_pipe in ["L", "J", "|"]: return True
			if offset[1] == 1:
				if next_pipe in ["7", "-"]: return True
		case "7":
			if offset[0] == 1:
				if next_pipe in ["L", "J", "|"]: return True
			if offset[1] == -1:
				if next_pipe in ["F", "-"]: return True

	return False

def naive_valid_pos(graph, next_pos, offset):
	next_pipe = graph[next_pos[0]][next_pos[1]]

	if next_pipe == "|" and offset[1] == 0:
		return True
	elif next_pipe == "-" and offset[0] == 0:
		return True
	elif next_pipe == "L" and offset[0] >= 0 and offset[1] <= 0:
		return True
	elif next_pipe == "J" and offset[0] >= 0 and offset[1] >= 0:
		return True
	elif next_pipe == "7" and offset[0] <= 0 and offset[1] >= 0:
		return True
	elif next_pipe == "F" and offset[0] <= 0 and offset[1] <= 0:
		return True
	
	return False

main()