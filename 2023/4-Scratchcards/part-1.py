def main():
	point_sum = 0

	with open("input.txt") as input:
		for card in input:
			winning = 0
			card = card.strip().split()
			card = card[2:]
			sep = card.index("|")
			winning_num = list(map(int, card[:sep]))
			current_num = list(map(int, card[sep+1:]))
			for i in current_num:
				for j in winning_num:
					if i == j:
						winning += 1
						break
			if winning != 0:
				point_sum += 2 ** (winning - 1)

	print(point_sum)
	return point_sum

main()