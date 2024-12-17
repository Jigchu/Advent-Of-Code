def main():
	total = 0
	with open("input.txt") as memory:
		for line in memory:
			line = "开" + line
			segments = line.split(sep="mul(")
			segments = segments[1:]
			for segment in segments:
				sub_segments = segment.split(sep=")")
				command = sub_segments[0]
				command = command.split(sep=",")
				if len(command) != 2:
					continue
				try:
					x, y = map(int, command)
				except ValueError:
					continue
				total += x*y
	
	print(total)

	return 0

if __name__ == "__main__":
	main()