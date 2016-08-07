"""
Pseudo random number generator using wichmann hill algorithm.
"""
import math

"""
normal distribution
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



"""
Using the abobe Uniform distribution random number generator to provide gausian
distribution number generator.
"""


class gaussian_prng:
    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev
        self.norm_prng = prng(120, 38, 74)
        self.spare = 0
        self.is_spare_ready = False

    def random(self):
        mul = 0
        if self.is_spare_ready :
            self.is_spare_ready = False
            return self.spare * self.std_dev + self.mean

        u = 0
        v = 0
        s = 0

        while True:
            u = self.norm_prng.random() * 2 - 1
            v = self.norm_prng.random() * 2 - 1
            s = u * u + v * v
            if s >= 1 or s is 0:
                break
        comp = math.sqrt(2.0 )#* math.log(s) / s)
        self.spare = v * mul
        self.is_spare_ready = True
        return self.mean + self.std_dev * u * mul


"""
my_prng = prng(120, 38, 74)

for i in range(5):
    print my_prng.random()
"""

my_gauss = gaussian_prng(4, 2)
for i in range(10):
	print my_gauss.random()

