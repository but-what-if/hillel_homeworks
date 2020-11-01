import random


class Unit:

    def __init__(self, name, clan, health=100, strength=10, agility=10, intelligence=10):
        self.name = name
        self.clan = clan
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def _health(self):
        self.health = random.randint(1, 100)
        return self.health

    def _strength(self):
        self.strength = random.randint(1, 10)
        return self.strength

    def _agility(self):
        self.agility = random.randint(1, 10)
        return self.agility

    def _intelligence(self):
        self.intelligence = random.randint(1, 10)
        return self.intelligence

    def healing(self):
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
        return self.health


class Mage(Unit):

    def __init__(self, name, clan, magic_type):
        super().__init__(name, clan)
        self.magic_type = magic_type
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intelligence = self._intelligence()

    def up_intelligence(self):
        if self.intelligence <= 9:
            self.intelligence += 1
        else:
            self.intelligence = 10
        return self.intelligence


mage = Mage('Lilia', 'People', 'Water')
print(f'{mage.name} is the Mage from {mage.clan} clan. Who owns {mage.magic_type} magic. Health: {mage.health}. Strength: {mage.strength}. Agility: {mage.agility}. Intelligence: {mage.intelligence}.')
print(f'{mage.name} ups her health {mage.healing()} and intelligence {mage.up_intelligence()}.')
print('===================================')


class Archer(Unit):

    def __init__(self, name, clan, bow_type):
        super().__init__(name, clan)
        self.bow_type = bow_type
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intelligence = self._intelligence()

    def up_agility(self):
        if self.agility <= 9:
            self.agility += 1
        else:
            self.agility = 10
        return self.agility


archer = Archer('Clod', 'People', 'Bow')
print(f'{archer.name} is the Archer from {archer.clan} clan. Who has a {archer.bow_type}. Health: {archer.health}. Strength: {archer.strength}. Agility: {archer.agility}. Intelligence: {archer.intelligence}.')
print(f'{archer.name} ups his health {archer.healing()} and agility {archer.up_agility()}.')
print('===================================')


class Knight(Unit):

    def __init__(self, name, clan, arms_type):
        super().__init__(name, clan)
        self.arms_type = arms_type
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intelligence = self._intelligence()

    def up_strength(self):
        if self.strength <= 9:
            self.strength += 1
        else:
            self.strength = 10
        return self.strength


knight = Knight('Lukas', 'People', 'Sword')
print(f'{knight.name} is the Knight from {knight.clan} clan. Who has a {knight.arms_type}. Health: {knight.health}. Strength: {knight.strength}. Agility: {knight.agility}. Intelligence: {knight.intelligence}.')
print(f'{knight.name} ups his health {knight.healing()} and strength {knight.up_strength()}.')
print('===================================')

