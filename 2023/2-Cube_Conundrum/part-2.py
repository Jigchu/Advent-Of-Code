from dataclasses import dataclass
import re


@dataclass
class SubGame:
	red: int
	green: int
	blue: int

def main():
	sum_of_power = 0
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
			
			lowest = [-1, -1, -1] # RGB respectively
			for sub_game in sub_games:
				if sub_game.red > lowest[0]:
					lowest[0] = sub_game.red
				if sub_game.green > lowest[1]:
					lowest[1] = sub_game.green
				if sub_game.blue > lowest[2]:
					lowest[2] = sub_game.blue
			power = lowest[0] * lowest[1] * lowest[2]
			sum_of_power += power
	print(sum_of_power)
	return sum_of_power

main()