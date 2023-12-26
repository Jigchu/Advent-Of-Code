from enum import Enum

cards = {
	"2": 2,	"3": 3, "4": 4,	"5": 5,	"6": 6,	"7": 7, "8": 8,	
	"9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14,
}

class HandType(Enum):
	KIND_FIVE = 0
	KIND_FOUR = 1
	FULL_HOUSE = 2
	KIND_THREE = 3
	PAIR_TWO = 4
	PAIR_ONE = 5
	HIGH = 6

class Hand:
	def __init__(self, hand: str, bid: int):
		self.hand = hand
		self.bid = bid
		self.type: HandType = self.get_type()

	def get_type(self):
		type: HandType = HandType.HIGH
		card_frquency = {}

		for card in self.hand:
			if card_frquency.get(card) == None:
				card_frquency[card] = 1
			else:
				card_frquency[card] += 1

		for card, frequency in card_frquency.items():
			match frequency:
				case 2:
					match type:
						case HandType.HIGH:
							type = HandType.PAIR_ONE
						case HandType.PAIR_ONE:
							type = HandType.PAIR_TWO
						case HandType.KIND_THREE:
							type = HandType.FULL_HOUSE
				case 3:
					match type:
						case HandType.HIGH:
							type = HandType.KIND_THREE
						case HandType.PAIR_ONE:
							type = HandType.FULL_HOUSE
				case 4:
					type = HandType.KIND_FOUR
				case 5:
					type = HandType.KIND_FIVE

		return type

def hand_key(hand: Hand):
	key = []
	for card in hand.hand:
		key.append(cards[card])
	return key

def main():
	total_winnings = 0
	hands: dict[HandType, list[Hand]] = {
		HandType.KIND_FIVE: [], HandType.KIND_FOUR: [], 
		HandType.FULL_HOUSE: [], HandType.KIND_THREE: [],
		HandType.PAIR_TWO: [], HandType.PAIR_ONE: [],
		HandType.HIGH: []
	}
	hand_num = 0

	with open("input.txt") as input:
		for hand in input:
			hand = hand.strip().split()
			h = Hand(hand=hand[0], bid=int(hand[1]))
			hands[h.type].append(h)
			hand_num += 1
	
	for type in hands:
		hands[type].sort(key=hand_key, reverse=True)

	for type, cards in hands.items():
		for card in cards:
			total_winnings += card.bid * hand_num
			hand_num -= 1

	print(total_winnings)
	return total_winnings

main()