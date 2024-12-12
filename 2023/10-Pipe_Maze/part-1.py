def main():
	maze = []
	start_pos = ()
	with open("input.txt") as input:
		for row_num, row in enumerate(input):
			row = list(row.strip())
			maze.append(row)
			try:
				col_num = row.index("S")
			except ValueError:
				continue
			start_pos = (row_num, col_num)

	start_pipe = find_start_pipe(maze, start_pos)
	maze[start_pos[0]][start_pos[1]] = start_pipe

	next_pos = [start_pos]
	total_steps = 0
	prev = (-1, -1)
	while True:
		curr = next_pos.pop()
		print(curr)
		if curr == start_pos and total_steps > 0:
			break
		next_pos.extend(next_valid_pipes(maze, curr, prev))
		prev = curr
		total_steps += 1
	
	farthest_steps = total_steps // 2
	print(farthest_steps)
	return farthest_steps

def next_valid_pipes(graph, curr, prev):
	next_valid = []
	curr_pipe = graph[curr[0]][curr[1]]
	pipe_offsets = {
		"|": [(-1, 0), (1, 0)],
		"-": [(0, -1), (0, 1)],
		"L": [(-1, 0), (0, 1)],
		"J": [(-1, 0), (0, -1)],
		"F": [(1, 0), (0, 1)],
		"7": [(1, 0), (0, -1)],
	}

	num_row = len(graph)
	num_col = len(graph[0])
	offsets = pipe_offsets[curr_pipe]
	
	for offset in offsets:
		next_pos = (curr[0]+offset[0], curr[1]+offset[1])
		if next_pos[0] in [-1, num_row] or next_pos[1] in [-1, num_col]:
			continue
		if next_pos == prev:
			continue
		next_valid.append(next_pos)

	return next_valid

def find_start_pipe(graph, start_pos):
	possible_pipes = {
		"N": { "S": "|", "E": "L", "W": "J", },
		"S": { "N": "|", "E": "F", "W": "7", },
		"E": { "N": "L", "S": "F", "W": "-", },
		"W": { "N": "J", "S": "7", "E": "-", },
	}
	num_row = len(graph)
	num_col = len(graph[0])
	offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	intersection = []
	
	for offset in offsets:
		adj_pos = (start_pos[0]+offset[0], start_pos[1]+offset[1])
		if adj_pos[0] in [-1, num_row] or adj_pos[1] in [-1, num_col]:
			continue
		if not intersecting(graph, adj_pos, offset):
			continue

		match offset:
			case (1, 0):
				intersection.append("S")
			case (-1, 0):
				intersection.append("N")
			case (0, 1):
				intersection.append("E")
			case (0, -1):
				intersection.append("W")

	return possible_pipes[intersection[0]][intersection[1]]
	
def intersecting(graph, next_pos, offset):
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