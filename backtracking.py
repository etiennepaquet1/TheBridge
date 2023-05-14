import math
import copy


class Bike:
    def __init__(self, v, x, y, j):
        self.v = v  # velocity of bike
        self.x = x  # horizontal position
        self.y = y  # lane of bike
        self.j = j  # how much airtime before landing (0 means it's on the ground)


class TestRunResult:
    def __init__(self, bikesSaved: int, groundCovered: int):
        self.bikesSaved = bikesSaved
        self.groundCovered = groundCovered



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
            JUMP(bikes)
        case 2:
            UP(bikes)
        case 3:
            DOWN(bikes)
        case 4:
            SLOW(bikes)
        case 5:
            WAIT(bikes)



def simulateTurn(bikes):
    bikesToRemove = []
    for bike in bikes:
        for pos in range(bike.x, min(bike.x + bike.v, len(lanes[0]) - 1)):  # range is exclusive at the upper bound so we need to add 1
            bike.x += 1
            if bike.j > 0:
                bike.j -= 1
            if bike.j == 0 and lanes[bike.y][pos] == "0":
                bikesToRemove.append(bike)
                break
    for bike in bikesToRemove:
        bikes.remove(bike)


    # # return the length of ground traveled
    # if len(bikes) == 0:
    #     return 0
    # else:
    #     return bikes[0].x


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
    global realBikes
    print(f"Testing actions: {actions}")
    testBikes = copy.deepcopy(realBikes)
    for action in actions:
        doAction(action, testBikes)
        simulateTurn(testBikes)

    groundCovered = testBikes[0].x if len(testBikes) > 0 else 0

    print(f"{len(testBikes)} bikes are still around and has covered a distance of {groundCovered} ")


    trr = TestRunResult(len(testBikes), groundCovered)

    return trr  # returns a testRunResult with the number of bikes and the ground covered



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
mostGroundCovered = 0

while not finishedTesting:
    result = testActionOrder(nextNActions)

    numberSaved = result.bikesSaved
    groundCovered = result.groundCovered

    if numberSaved > mostBikesSaved or (numberSaved == mostBikesSaved and groundCovered > mostGroundCovered):
        bestActionOrder = nextNActions
        mostBikesSaved = numberSaved
        mostGroundCovered = groundCovered
    incrementActionOrder(nextNActions)


# n = testActionOrder([3, 3, 3, 3, 3])


print(f"Best action order: {bestActionOrder}")
















