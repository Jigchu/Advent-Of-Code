"""
Please run part-1 before part-2 because part-1 writes the wrong updates into wrong.txt
I was too lazy to put essentially the whole of part-1 into part-2
"""

class OrderingRule:
	def __init__(self):
		self.before = []
		self.after = []

class Node:
	def __init__(self, value):
		self.value = value
		self.next: Node = None
		self.prev: Node = None

sequence: dict[int, OrderingRule] = {}

def main():
	total = 0
	updates: list[list[int]] = []

	with open("input.txt") as input:
		for line in input:
			line = line.strip()
			if line == "":
				break
			before, after = map(int, line.split(sep="|"))
			sequence[before] = sequence.get(before) or OrderingRule()
			sequence[after] = sequence.get(after) or OrderingRule()
			sequence[before].after.append(after)
			sequence[after].before.append(before)

	with open("wrong.txt") as wrong:
		for line in wrong:
			update = list(map(int, line.split(sep=",")))
			updates.append(update)
		
	for update in updates:
		new_update = order_update(update)
		total += new_update[len(new_update)//2]

	print(total)

	return 0

# We use a linked list to make moving values easier
def order_update(update):
	linked_update = Node(update[0])
	update = update[1:]

	for page in update:
		curr = linked_update
		direction = None
		while True:
			if page in sequence[curr.value].after:
				if direction == "L":
					# This is complicated on purpose :3
					tmp = Node(page)
					tmp.next = curr.next
					tmp.next.prev = tmp
					tmp.prev = curr
					tmp.prev.next = tmp
					break
				direction = "R"

			if page in sequence[curr.value].before:
				if direction == "R":
					tmp = Node(page)
					tmp.next = curr
					tmp.prev = curr.prev
					tmp.next.prev = tmp
					tmp.prev.next = tmp
					break
				direction = "L"
			
			if direction == None or direction == "R":
				if curr.next == None:
					tmp = Node(page)
					tmp.prev = curr
					curr.next = tmp
					break
				curr = curr.next
			if direction == "L":
				if curr.prev == None:
					tmp = Node(page)
					linked_update = tmp
					tmp.next = curr
					curr.prev = tmp
					break
				curr = curr.next

	new_update = []
	curr = linked_update
	while curr:
		new_update.append(curr.value)
		curr = curr.next

	return new_update


if __name__ == "__main__":
	main()