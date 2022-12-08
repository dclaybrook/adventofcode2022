## Day 2: Advent of Code 2022

filename = "input.txt"
guide_array = []
opponentScore = []
opponentWins = 0
opponentLosses = 0
myScore = []
myWins = 0
myLosses = 0
draws = 0

with open(filename) as file:
    guide = file.readlines()  # Read the input file as an array

guide = [x.strip() for x in guide]  # Strip the whitespace chars from the array
for round in guide:
    guide_array.append(round.split())  # Create a 2D array of rounds and strategic play

def getShapeName(shape):
    shapes = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors"
    }
    return shapes.get(shape)

def getShapeValue(shape_name):
    shape_values = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }
    return shape_values.get(shape_name)

def getValue(shape):
    return getShapeValue(getShapeName(shape))

def winner_opponent(a, b):
    global myWins
    global myLosses
    global opponentWins
    global opponentLosses
    opponentScore.append(a+6)
    myScore.append(b+0)
    opponentWins += 1
    myLosses += 1
    #print("Opponent Won")

def winner_me(a, b):
    global myWins
    global myLosses
    global opponentWins
    global opponentLosses
    opponentScore.append(a+0)
    myScore.append(b+6)
    myWins += 1
    opponentLosses += 1
    #print("I Won")

def winner_draw(a, b):
    global draws
    opponentScore.append(a+3)
    myScore.append(b+3)
    draws += 1
    #print("Draw")

def processResult(a, b):
    if a == 1 and b == 3:  #Rock beats Scissors
        winner_opponent(a, b)
    elif a == 3 and b == 1:  #Rock beats Scissors
        winner_me(a, b)
    elif a == 3 and b == 2:  #Scissors beat Paper
        winner_opponent(a, b)
    elif a == 2 and b == 3:  #Scissors beat Paper
        winner_me(a, b)
    elif a == 2 and b == 1:  #Paper beats Rock
        winner_opponent(a, b)
    elif a == 1 and b == 2:  #Paper beats Rock
        winner_me(a, b)
    elif a == b:
        winner_draw(a, b)
    else:
        print("Something weird happened")

for hand in guide_array:
    a = getValue(hand[0])  # Opponent's Hand
    b = getValue(hand[1])  # My Hand
    processResult(a,b)

print("Total rounds:", len(guide_array))
print("My Score:", sum(myScore))
print("My Wins:", myWins)
print("My Losses:", myLosses)
print("Opponent Score:", sum(opponentScore))
print("Opponent Wins:", opponentWins)
print("Opponent Losses:", opponentLosses)
print("Draws:", draws)