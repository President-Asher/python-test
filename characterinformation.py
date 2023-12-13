import character

def main():
    hero_name= ''
    hero_id = ''
    hero_shift = 0
    hero_pay = 0.0

    boss_name= ''
    boss_id = ''
    boss_level = 0
    boss_hp = 0.0
    boss_attack_damage = 0.0
    boss_lifespan = 0.0
    print("Hero Data Entry")
    print("---------------")
    hero_name = input("Enter the hero name: ")
    hero_id = input("Enter the character ID number: ")
    hero_level = int(input("Enter the hero level: "))
    hero_loot = float(input("Enter the hero loot value: "))

    hero = character.Hero(hero_name, hero_id, hero_level, hero_loot)

    print(" ")
    print("Boss Data Entry")
    print("---------------")
    boss_name = input("Enter the boss name: ")
    boss_id = input("Enter the character ID number: ")
    boss_level = int(input("Enter the boss level: "))
    boss_hp = float(input("Enter the boss hp: "))
    boss_attack_damage = float(input("Enter the boss attack damage: "))

    boss = character.Boss(boss_name, boss_id, boss_level, boss_hp, boss_attack_damage)

    print(" ")
    print("Hero information:")
    print(f"Name: {hero_name}")
    print(f"ID number: {hero_id}")
    print(f"Level: {hero_level}")
    print(f"Loot: ${hero_loot}")

    print(" ")
    print("Boss information: ")
    print(f"Name: {boss_name}")
    print(f"ID number: {boss_id}")
    print(f"Level: {boss_level}")
    print(f"HP: {boss_hp}")
    print(f"Attack Damage: {boss_attack_damage}")
    print(f"Lifespan: {boss.get_lifespan()} attacks")

if __name__ == '__main__':
    main()