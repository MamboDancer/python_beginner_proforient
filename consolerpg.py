import random

player_hp = 10
player_attack = 2
player_defense = 0
potions = 0
level = 1
money = 0
game = True


def shop():
    pass


def encounter():
    global game
    global player_hp
    global level
    enemy_name = random.choice(["Rat", "Zombie", "Skeleton", "Dragon", "Bat"])
    enemy_hp = random.randint(1, 7) * level
    enemy_attack = random.randint(1, 5) * level
    while enemy_hp > 0 and player_hp > 0:
        print("[" + enemy_name + "]")
        print("[Enemy HP]: " + str(enemy_hp))
        print("[Enemy attack]: " + str(enemy_attack))

        print("What to do?")
        print("1. Attack")
        print("2. Run away")
        if int(input()) == 1:
            print("You attacked " + enemy_name + " with " + str(player_attack) + " damage")
            enemy_hp -= player_attack
            attack = enemy_attack - player_defense
            if attack < 0:
                attack = 0
            player_hp -= attack
            print("[PLAYER] HP: " + str(player_hp))

    if player_hp <= 0:
        print("Game Over!")
        game = False
    else:
        print("You won!")
        level += 1


def heal():
    pass


def go_further():
    print("Moving forward!")
    direction = random.randint(0, 100)
    if direction > 80:
        shop()
    else:
        encounter()


def show_stats():
    print("HP: ", player_hp)
    print("Attack: ", player_attack)
    print("Defense: ", player_defense)
    print("Level: ", level)
    print("Balance: ", money)


while game:
    show_stats()
    print("1. Go further")
    print("2. Heal")
    print("3. Quit")
    choice = int(input(""))
    if choice == 1:
        go_further()
    if choice == 2:
        heal()
    if choice == 3:
        game = False