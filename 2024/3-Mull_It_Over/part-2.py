def main():
	total = 0
	with open("input.txt") as memory:
		for line in memory:
			do = []
			doless = line.split(sep="do()")
			for mem in doless:
				mem = "开" + mem
				sub_mem = mem.split(sep="don't()")
				do_ful = sub_mem[0]
				do_ful = list(do_ful)
				do_ful.remove("开")
				do_ful = "".join(do_ful)
				do.append(do_ful)
			for mem in do:
				mem = "开" + mem
				segments = mem.split(sep="mul(")
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