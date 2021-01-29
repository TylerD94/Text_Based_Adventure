from Classes.Player import Player
from Classes.Fight import GuardA

spellbook = [{}]

items = [{}]

# basic story commands
fight = 'fight'
leave = 'leave'
door = 'door'
ladder = 'ladder'
open_chest = 'open chest'

BATTLE = False

print('Welcome to the story.')
print('What is your name?')
name = input('>>> ')

player = Player(name, 420, 80, 50, [{'spell_power'}], spellbook, items)

print(f'Welcome to the game {name}.')
print('\n\n\n')

print('You arrive at the dungeon. From the outside, it seems to be a simple cave, with a guard outside.')
print('Will you fight, or leave?')

choice = input('>>> ')
if choice in fight:
    BATTLE = True
    guard_a = GuardA(200, 30)
    while BATTLE:
        print(player.get_hp())
        print(guard_a.get_hp())
        player.choose_actions()

        choice = input('>>> ')
        index = int(choice) - 1

        if index == 0:
            player_damage = player.generate_damage()
            guard_a.take_damage(player_damage)
        elif index == 1:
            print("You don't have any spells yet!")
            continue
        elif index == 2:
            print("You don't have any items yet!")
            continue

        enemy_damage = guard_a.generate_damage()
        player.take_damage(enemy_damage)

        if guard_a.get_hp() == 0:
            print("You have defeated the guard!")
            BATTLE = False
        elif player.get_hp() == 0:
            print("GAME OVER.")
            exit()

if choice in leave:
    print("Just gonna walk away? Wack.")
    exit()

print('You defeat the guard and head inside. The faint light from torches on the wall show a door to your left,'
      'and a ladder heading down straight ahead.')
choice = input('>>> ')

if choice in ladder:
    print('You descend the ladder into a storeroom full of barrels and boxes. Most are not important,'
          'but you find a chest along the far wall.')
    if choice in open_chest:
        print('You open the chest and find a silver key and a scroll. The scroll explains how to cast the'
              'Fire spell.')
        spellbook.add = [{'spell_name': 'Fire', 'spell_power': '20', 'spell_cost': '10'}]
        items.add = [{'item_name': 'Silver Key', 'item_description': 'An ornate silver key.', 'item_potency': '0'}]
        print('You obtained the Silver Key!')
        print('You obtained the Fire spell!')
        print('\n\n\n')
        print('As you turn to leave, a guard comes down the ladder. Time for a fight!')

        BATTLE = True
        guard_a = GuardA(200, 30)
        while BATTLE:
            print(player.get_hp(), player.get_max_hp(), player.get_mp(), player.get_max_mp())
            print(guard_a.get_hp())
            player.choose_actions()

            choice = input('>>> ')
            index = int(choice) - 1

            if index == 0:
                player_damage = player.generate_damage()
                guard_a.take_damage(player_damage)
            elif index == 1:
                player.choose_spell()
                spell_choice = int(input('>>> ')) - 1

                spell = player.spellbook[spell_choice]
                magic_damage = player.generate_magic_damage

                cost = [{'spell_cost'}]

                if cost > player.get_mp():
                    print("You can't cast that right now...")
                    continue

                player.reduce_mp(cost)
                GuardA.take_damage(magic_damage)


            elif index == 2:
                print("You don't have any items yet!")
                continue

            enemy_damage = guard_a.generate_damage()
            player.take_damage(enemy_damage)

            if guard_a.get_hp() == 0:
                print("You have defeated the guard!")
                BATTLE = False
            elif player.get_hp() == 0:
                print("GAME OVER.")
                exit()

    if choice in ladder:
        print('You climb back up the ladder. You see the cave entrance straight ahead, and the door to your right.')