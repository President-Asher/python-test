class Character:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

class Boss(Character):
    def __init__(self, name, id_number, level, hp, attack_damage):

        Character .__init__(self, name, id_number)

        self.__level = level
        self.__hp = hp
        self.__attack_damage = attack_damage
        self.__lifespan = 0

    def set_level(self, level):
        self.__level = level

    def set_hp(self, hp):
        self.__hp = hp

    def set_attack_damage(self, attack_damage):
        self.__attack_damage = attack_damage

    def set_lifespan(self, lifespan):
        self.__lifespan = lifespan

    def get_level(self):
        return self.__level

    def get_hp(self):
        return self.__hp

    def get_attack_damage(self):
        return self.__attack_damage

    def get_lifespan(self):
        return (self.__hp / 300)

class Hero(Character):
    def __init__(self, name, id_number, level, loot):
        Character.__init__(self, name, id_number)

        self.__level = level
        self.__loot = loot

    def set_level(self, level):
        self.__level = level

    def set_pay_rate(self, __loot):
        self.__loot = loot


    def get_level(self):
        return self.__level

    def get_loot(self):
        return self.__loot