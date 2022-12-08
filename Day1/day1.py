## Day 1: Advent of Code 2022

from itertools import groupby

filename = "input.txt"
allItems = []
calorieArray = []

with open(filename) as file:
    allItems = file.readlines() # Read the input file as an array

allItems = [x.strip() for x in allItems]  # Strip the whitespace chars from the array
allItemsArray = [list(sub) for ele, sub in groupby(allItems, key = bool) if ele]  # split the array into a 2D array per elf

for elf in allItemsArray:
    elf = list(map(int, elf)) # Convert each elf's items into an integer
    calories = sum(elf)  # Sum the calories
    calorieArray.append(calories)  # Append to the total Calorie Array

sortedCalories = sorted(calorieArray, reverse=True)
topThree = sortedCalories[0]+sortedCalories[1]+sortedCalories[2]

#print("Array of each Elf's calories:", calorieArray)
print("Total number of elves:", len(allItemsArray))
print("Elf", calorieArray.index(max(calorieArray))+1, "has the most calories with", max(calorieArray))
print("The top three Elves have a combined", topThree, "calories.")