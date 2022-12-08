## Day 3 (parts 1 and 2): Advent of Code 2022

import string

filename = "input.txt"

def get_repeated_char(string1, string2):
	for char in string1:
		if string2.count(char) > 0:
			return char
	return False

def get_group_badge(string1, string2, string3):
	for char in string1:
		if string2.count(char) > 0:
			if string3.count(char) > 0:
				return char
	return False

def get_item_priority(item):
	return string.ascii_letters.index(item)+1

with open(filename) as inputfile:
	rucksacks = inputfile.read().splitlines() 

def check_item_compartments(rucksacks):
	doubledItems = []
	itemSum = 0
	for items in rucksacks:
		compartment1 = items[:len(items)//2]
		compartment2 = items[len(items)//2:]
		doubledItem = (get_repeated_char(compartment1,compartment2))
		doubledItems.append(doubledItem)
		itemSum += get_item_priority(doubledItem)
	print("The sum of the sum of the priorities of these",len(doubledItems),"item types is:", itemSum)
	return True

def get_badge_priority(rucksacks):
	i = 0
	groupSum = 0
	while(i < len(rucksacks)):
		groupBadge = get_group_badge(rucksacks[i],rucksacks[i+1],rucksacks[i+2])
		groupSum += get_item_priority(groupBadge)
		i += 3
	print("The sum of the sum of the group priorities is:", groupSum)
	return True

check_item_compartments(rucksacks)
get_badge_priority(rucksacks)
