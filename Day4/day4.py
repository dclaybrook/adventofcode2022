## Day 4 (part 1 and 2): Advent of Code 2022

filename = "input.txt"

with open(filename) as inputfile:
	assignments = inputfile.read().splitlines()

def get_range_set(pair):
	start = pair[0]
	stop = pair[1]+1
	return set(range(start, stop))

def camp_cleanup(assignments):
	contained = 0
	overlap = 0
	for pair in assignments:
		pairing = pair.split(",")
		pair1 = get_range_set(list(map(int, pairing[0].split("-"))))
		pair2 = get_range_set(list(map(int, pairing[1].split("-"))))
		if check_subset(pair1, pair2):
			contained += 1
		if check_overlap(pair1, pair2):
			overlap += 1
	return [contained,overlap]

def check_overlap(pair1, pair2):
	if len(pair1.intersection(pair2)) > 0:
		return True
	else:
		return False

def check_subset(pair1, pair2):
	if pair1.issubset(pair2) or pair1.issuperset(pair2):
		return True
	else:
		return False

print("Of", len(assignments), "assignments, there are", camp_cleanup(assignments)[0], "fully-contained ranges")
print("Of", len(assignments), "assignments, there are", camp_cleanup(assignments)[1], "overlapping ranges")