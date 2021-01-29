import random

class GuardA:
    def __init__(self, hp, atk):
        self.name = "Guard A"
        self.hp = hp
        self.max_hp = hp
        self.low_atk = atk - 5
        self.high_atk = atk + 5

    def generate_damage(self):
        return random.randrange(self.low_atk, self.high_atk)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        elif self.hp >= self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp