class Scratchcard:
	def __init__(self, matching: int):
		self.matching = matching
		self.instance = 1
	
	def add_instances(self, instances: int):
		self.instance += instances

def main():
	total_scratchcards = 0
	scratchcards: list[Scratchcard] = []

	with open("input.txt") as input:
		for card in input:
			matching = 0
			card = card.strip().split()
			card = card[2:]
			sep = card.index("|")
			matching_num = list(map(int, card[:sep]))
			current_num = list(map(int, card[sep+1:]))
			for i in current_num:
				for j in matching_num:
					if i == j:
						matching += 1
						break
			scratchcards.append(Scratchcard(matching=matching))
	
	for i, card in enumerate(scratchcards):
		if card.matching == 0:
			pass
		next = scratchcards[i+1:]
		for j, next_card in enumerate(next):
			if j >= card.matching:
				break
			next_card.add_instances(card.instance)
	
	for card in scratchcards:
		total_scratchcards += card.instance

	print(total_scratchcards)
	return total_scratchcards


main()