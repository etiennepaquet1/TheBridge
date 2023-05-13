import math


class Bike:
    def __init__(self, v, x, y, j):
        self.v = v  # velocity of bike
        self.x = x  # horizontal position
        self.y = y  # lane of bike
        self.j = j  # how much airtime before landing (0 means it's on the ground)


def SPEED(bikes):
    for bike in bikes:
        bike.v += 1


def SLOW(bikes):
    for bike in bikes:
        if bike.v > 0:
            bike.v -= 1


def JUMP(bikes):
    for bike in bikes:
        bike.j += v


def WAIT(bikes):
    pass


def DOWN(bikes):
    # sort the bikes by y-position
    bikes = sorted(bikes, key=lambda bike: bike.y,  reverse=True)
    for bike in bikes:
        if bike.y < 3 and not any(b.y == bike.y+1 for b in bikes):
            bike.y += 1


def UP(bikes):
    # sort the bikes by y-position
    bikes = sorted(bikes, key=lambda bike: bike.y,  reverse=False)
    for bike in bikes:
        if bike.y > 0 and not any(b.y == bike.y-1 for b in bikes):
            bike.y -= 1


def doAction(n: int, bikes: [Bike]):
    match n:
        case 0:
            SPEED(bikes)
        case 1:
            SLOW(bikes)
        case 2:
            JUMP(bikes)
        case 3:
            WAIT(bikes)
        case 4:
            DOWN(bikes)
        case 5:
            UP(bikes)


def simulateTurn(bikes):
    bikesToRemove = []
    for bike in bikes:
        for pos in range(bike.x, min(bike.x + bike.v + 1, len(lanes[0]) - 1)):  # range is exlusive at the upper bound so we need to add 1
            bike.x += 1
            if bike.j > 0:
                bike.j -= 1
            if bike.j == 0 and lanes[bike.y][pos] == "0":
                bikesToRemove.append(bike)
                break
    for bike in bikesToRemove:
        bikes.remove(bike)


def printLanesWithBikes():
    lanesList = []
    for lane in lanes:
        lanesList += [list(lane)]
    for bike in realBikes:
        lanesList[bike.y][bike.x] = "J" if bike.j else "B"
    for lane in lanesList:
        print("".join(lane))
    print()


# takes as input the action order presented and returns the number of bikes left after the actions are taken
def testActionOrder(actions: [int]):
    print(f"Testing actions: {actions}")
    testBikes = realBikes.copy()
    for action in actions:
        doAction(action, testBikes)
        simulateTurn(testBikes)
    print(f"{len(testBikes)} bikes are still around")
    return len(testBikes)


def incrementActionOrder(nextNActions: [int]):
    global finishedTesting
    cursor = len(nextNActions) - 1
    done = False
    nextNActions[cursor] += 1
    while not done:
        if nextNActions[cursor] == 6:
            nextNActions[cursor] = 0
            cursor -= 1
            nextNActions[cursor] += 1
            # if every possibility has been tested
            if cursor == 0 and nextNActions[cursor] == 6:
                done = True
                finishedTesting = True
        else:
            done = True



n = 5  # number of actions in the future to foresee

v = 0
x = 0

realBikes = [Bike(0, 0, 0, 0),
         Bike(0, 0, 1, 0),
         Bike(0, 0, 2, 0),
         Bike(0, 0, 3, 0)]

bikesNeeded = 1


l0 = "................000000000........00000........000.............00."
l1 = ".0.0..................000....000......0.0..................00000."
l2 = "....000.........0.0...000................000............000000.0."
l3 = "............0.000000...........0000...............0.0.....000000."

lanes = [l0, l1, l2, l3]



'''
w = testActionOrder(nextNActions)
print(w)
'''


# loop for one turn:

finishedTesting = False

nextNActions = 5 * [0]
bestActionOrder = nextNActions

mostBikesSaved = 0


while not finishedTesting:

    numberSaved = testActionOrder(nextNActions)
    if numberSaved > mostBikesSaved:
        bestActionOrder = nextNActions
        mostBikesSaved = numberSaved
    if numberSaved == len(realBikes):
        break
    incrementActionOrder(nextNActions)
print(f"Best action order: {bestActionOrder}")
















