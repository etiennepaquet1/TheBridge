class Bike:
    def __init__(self, v: int, x: int, y: int, j: int):
        self.v = v  # velocity of bike
        self.x = x  # horizontal position
        self.y = y  # lane of bike
        self.j = j  # how much airtime before landing (0 means it's on the ground)
