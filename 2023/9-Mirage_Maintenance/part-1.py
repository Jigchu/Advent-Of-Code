def main():
	extrapolated_total = 0
	report = []
	report_num = 0
	with open("input.txt") as input:
		for row in input:
			row = list(map(int, row.strip().split()))
			entry = []
			entry.append(row)
			while True:
				sequence_diff = []
				for i, n in enumerate(row):
					if i == 0:
						continue
					sequence_diff.append(row[i] - row[i-1])
				entry.append(sequence_diff)
				row = sequence_diff
				condition = True
				for n in sequence_diff:
					if n != 0:
						condition = False
				if condition:
					break
			entry.reverse()
			report.append(entry)
			report_num += 1

	for i in range(report_num):
		entry = report[i]
		num = 0
		for i in range(len(entry)):
			if i == 0:
				entry[i].append(entry[i][0])
				continue
			l1 = len(entry[i-1])
			l2 = len(entry[i])
			entry[i].append(entry[i][l2-1] + entry[i-1][l1-1])
			if i == len(entry) - 1:
				num = entry[i][l2]
		extrapolated_total += num
		
	print(extrapolated_total)
	return extrapolated_total

main()