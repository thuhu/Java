"""
Pseudo random number generator using wichmann hill algorithm.
"""
import math

"""
Global random seeds
"""
class prng:
    def __init__(self, inti_x=1, inti_y=1, inti_z=1):
        self.x = inti_x
        self.y = inti_y
        self.z = inti_z

    def random(self):
        # First generator
        self.x = 171 * (self.x % 177) - 2 * (self.x / 177)
        if self.x < 0:
            self.x += 30269
        # Second generator
        self.y = 172 * (self.y % 176) - 35 * (self.y / 176)
        if self.y < 0:
            self.y += 30307
        # Thrid generator
        self.z = 170 * (self.z % 178) - 63 * (self.z / 178)
        if self.z < 0:
            self.z += 30323

        # Combine
        tmp = (self.x/30269.0) + self.y/30307.0 + self.z/30323.0
        tmp -= math.trunc(tmp)
        return tmp

my_prng = prng(120, 38, 54)

for i in range(5):
    print my_prng.random()
