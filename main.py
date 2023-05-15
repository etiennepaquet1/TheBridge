import copy
import time
from Bike import Bike as Bike
from TestRunResult import TestRunResult as TestRunResult


from testcase5 import lanes, l0, l1, l2, l3, realBikes, bikesNeeded


def SPEED(bikes):
    for bike in bikes:
        bike.v += 1


def SLOW(bikes):
    for bike in bikes:
        if bike.v > 0:
            bike.v -= 1


def JUMP(bikes):
    for bike in bikes:
        bike.j += bike.v


def WAIT(bikes):
    pass


def DOWN(bikes):
    # sort the bikes by y-position
    bikes = sorted(bikes, key=lambda bike: bike.y, reverse=True)
    for bike in bikes:
        if bike.y < 3 and not any(b.y == bike.y + 1 for b in bikes):
            bike.y += 1


def UP(bikes):
    # sort the bikes by y-position
    bikes = sorted(bikes, key=lambda bike: bike.y, reverse=False)
    for bike in bikes:
        if bike.y > 0 and not any(b.y == bike.y - 1 for b in bikes):
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
        for pos in range(bike.x, min(bike.x + bike.v + 1,
                                     len(lanes[0]) - 1)):  # range is exclusive at the upper bound, so we need to add 1
            if bike.j > 0:
                bike.j -= 1
            if bike.j == 0 and lanes[bike.y][pos] == "0":
                bikesToRemove.append(bike)
                break
            bike.x += 1
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
    # print(f"Testing actions: {actions}")
    testBikes = copy.deepcopy(realBikes)
    for action in actions:
        doAction(action, testBikes)
        simulateTurn(testBikes)

    groundCovered = testBikes[0].x - realBikes[0].x if len(testBikes) > 0 else 0

    # print(f"{len(testBikes)} bikes are still around and has covered a distance of {groundCovered} ")

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


def bikeCrashes(bike):  # does the bike crash during the next turn?
    lane = lanes[bike.y]




    pass


n = 4  # number of actions in the future to foresee



for turn in range(50):
    # loop for one turn

    # print the lanes
    printLanesWithBikes()

    # if we have crossed the line, terminate the program
    if realBikes[0].x == len(l1) - 1:
        print("nicely done")
        break


    # find the best action
    finishedTesting = False
    nextNActions = n * [0]
    bestActionOrder = nextNActions.copy()
    bestResult = TestRunResult(0, 0)
    t0 = time.time_ns()

    while not finishedTesting:
        result = testActionOrder(nextNActions)

        numberSaved = result.bikesSaved
        groundCovered = result.groundCovered

        if bestResult.isBetterResult(result):
            bestActionOrder = copy.deepcopy(nextNActions)
            bestResult = TestRunResult(numberSaved, groundCovered)
        incrementActionOrder(nextNActions)

    t1 = time.time_ns()

    print(f"Best action order: {bestActionOrder} with {bestResult.bikesSaved} bikes saved and {bestResult.groundCovered} unit(s) covered")
    print(f"time passed: {(t1 - t0)/1000000000}")
    print("\n")


    # execute action on real bikes
    doAction(bestActionOrder[0], realBikes)
    simulateTurn(realBikes)

    # end the simulation if realBikes is empty
    if len(realBikes) < bikesNeeded:
        print("game over, all our bikes have crashed")
        break

