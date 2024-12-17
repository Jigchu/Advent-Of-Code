import sys

def main():
	safe_reports = 0
	reports: list[list] = []
	with open("input.txt") as input:
		for line in input:
			report = list(map(int, line.strip().split()))
			reports.append(report)

	for report in reports:
		if safe(report.copy()):
			safe_reports += 1

	print(safe_reports)
	return 0

def safe(report: list) -> bool:
	safe = True

	increasing = report[0] - report[1] > 0
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
		return safe
	
	for i in range(len(report)):
		report_copy = report.copy()
		report_copy.pop(i)
		increasing = report_copy[0] - report_copy[1] > 0
		for j in range(len(report_copy)):
			safe = False
			try:
				diff = report_copy[j] - report_copy[j+1]
			except IndexError:
				pass
			if diff < 0 and increasing:
				break
			if diff > 0 and not increasing:
				break
			if abs(diff) < 1 or abs(diff) > 3:
				break
			safe = True
			
		if safe:
			return safe
	

if __name__ == "__main__":
	main()