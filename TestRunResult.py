class TestRunResult:
    def __init__(self, bikesSaved: int, groundCovered: int):
        self.bikesSaved = bikesSaved
        self.groundCovered = groundCovered

    # compare test run to a second results object and return if the argument is better than the caller object.
    def isBetterResult(self, newResult):
        global l0
        global realBikes
        global bikesNeeded
        global turn
        # remainingGround = len(l0) - realBikes[0].x
        groundValueConstant = 20  # groundValueConstant reduces the relative value of ground to avoid sacrificing bikes when there is no need to

        try:
            # oldScore = (self.groundCovered - remainingGround) * ((-40 / (turn - 51)) + 1) / abs(self.bikesSaved - bikesNeeded)
            # newScore = (newResult.groundCovered - remainingGround) * ((-40 / (turn - 51)) + 1) / abs(newResult.bikesSaved - bikesNeeded)



            # oldScore = self.groundCovered * self.bikesSaved
            # newScore = newResult.groundCovered * newResult.bikesSaved

            oldScore = (self.groundCovered + groundValueConstant) * self.bikesSaved
            newScore = (newResult.groundCovered + groundValueConstant) * newResult.bikesSaved


        except ZeroDivisionError:
            # this means the new score saves 0 bikes
            return False

        return newScore > oldScore and newResult.groundCovered > 3
