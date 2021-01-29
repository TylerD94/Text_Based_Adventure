import random

class Spells:
    def __init__(self, name, dmg, cost):
        self.name = name
        self.dmg_low = dmg - 5
        self.dmg_high = dmg + 5
        self.cost = cost

    def generate_matk(self):
        return random.randrange(self.dmg_low, self.dmg_high)

    def get_cost(self):
        return self.cost
