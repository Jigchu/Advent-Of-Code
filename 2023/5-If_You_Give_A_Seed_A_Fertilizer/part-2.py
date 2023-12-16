class State:
	def __init__(self, start: int, end: int, m: int):
		self.map = m 
		self.start = start
		self.end = end

	@classmethod
	def init(cls, start: int, range_len: int, m: int):
		s = State(0, 0, 0)
		s.map = m
		s.start = start
		s.end = start + range_len
		return s
	
	def __str__(self):
		return f"[{self.map}, {self.start}, {self.end}]"

class Map:
	def __init__(self, destination, source_start, range_len):
		self.destination = destination
		self.source_start = source_start
		self.source_end = source_start + range_len
	
	def __str__(self):
		return f"[{self.destination}, {self.source_start}, {self.source_end}]"

def main():
	states: list[State] = []
	maps: list[list[Map]] = []
	map_num = 0
	state_num = 0

	with open("input.txt") as input:
		new_map = False
		for row in input:
			row = row.strip()
			if "seeds:" in row:
				row = list(map(int, row.split()[1:]))
				for i, n in enumerate(row):
					if i%2 != 0:
						states.append(State.init(row[i-1], row[i], 0))
						state_num += 1
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
				m = Map(destination=row[0], source_start=row[1], range_len=row[2])
				maps[map_num-1].append(m)
				continue
	
	i = 0
	while i < state_num:
		while states[i].map < map_num:
			for m in maps[states[i].map]:
				start = states[i].start in range(m.source_start, m.source_end)
				end = (states[i].end - 1) in range(m.source_start, m.source_end)
				if states[i].end <= m.source_start or states[i].start >= m.source_end:
					continue
				if not start:
					new_state = State(start=states[i].start, end=m.source_start, m=states[i].map)
					states[i].start = m.source_start
					states.append(new_state)
					state_num += 1
				if not end:
					new_state = State(start=m.source_end, end=states[i].end, m=states[i].map)
					states[i].end = m.source_end
					states.append(new_state)
					state_num += 1
				start = states[i].start in range(m.source_start, m.source_end)
				end = (states[i].end - 1) in range(m.source_start, m.source_end)
				if start and end:
					offset = m.destination - m.source_start
					states[i].start += offset
					states[i].end += offset
				break
			states[i].map += 1
		i += 1
	
	min_location = -1
	for state in states:
		if min_location == -1 or min_location > state.start:
			min_location = state.start
	print(min_location)
	return min_location
		
main()