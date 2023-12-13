from dataclasses import dataclass
import re


@dataclass
class SubGame:
	red: int
	green: int
	blue: int

def main():
	sum_of_id = 0
	with open("input.txt") as input:
		for game in input:
			game = re.sub("[,:]", "", game)
			game = re.sub(";", " ; ", game).split()
			id: int = 0
			sub_games: list[SubGame] = []
			length = 0
			new_sub_game = True

			for index, word in enumerate(game):
				if word == "Game":
					id = int(game[index+1])
				if new_sub_game:
					new_sub = SubGame(0, 0, 0)
					sub_games.append(new_sub)
					length += 1
					new_sub_game = False
				if word == ";":
					new_sub_game = True
				if word == "red":
					sub_games[length-1].red = int(game[index-1])
				if word == "green":
					sub_games[length-1].green = int(game[index-1])
				if word == "blue":
					sub_games[length-1].blue = int(game[index-1])
			
			passes = True
			for sub_game in sub_games:
				if sub_game.red > 12 or sub_game.blue > 14 or sub_game.green > 13:
					passes = False
			sum_of_id += id if passes else 0
	print(sum_of_id)
	return sum_of_id

main()