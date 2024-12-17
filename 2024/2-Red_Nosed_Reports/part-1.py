def main():
	safe_reports = 0

	with open("error.txt") as input:
		for line in input:
			report = list(map(int, line.strip().split()))
			increasing = report[0] - report[1] > 0
			safe = True
			for i in range(len(report)):
				try:
					diff = report[i] - report[i+1]
				except IndexError:
					pass
				if diff < 0 and increasing:
					safe = False
				if diff > 0 and not increasing:
					safe = False
				if abs(diff) < 1 or abs(diff) > 3:
					safe = False
			if safe:
				safe_reports += 1
			elif not safe:
				print(*report)

	print(safe_reports)

	return 0

if __name__ == "__main__":
	main()