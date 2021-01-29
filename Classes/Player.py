import random

class Player:
    def __init__(self, name, hp, mp, atk, spellbook, items):
        # set core stats
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp

        # Start damage calculations
        self.atk_low = atk - 10
        self.atk_high = atk + 10

        self.spellbook = spellbook
        self.items = items

        self.actions = ["Fight", "Spells", "Items"]

    # fuck em up boi
    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    # Sometimes we get hit, we gotta get rekt too.
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        elif self.hp >= self.max_hp:
            self.hp = self.max_hp

    def choose_actions(self):
        i = 1
        print("Actions:")
        for items in self.actions:
            print(str(i) + ':', items)
            i += 1

    def choose_spell(self):
        i = 1
        print("Spellbook")
        for spell in self.spellbook:
            print(str(i) + ':', spell.name, 'Cost :', str(spell.cost))
            i += 1

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost
