# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location, name = "Georgina", stamina = 5, weapon_collection = [], health = 50):
        self.name = name
        self.location = location
        self.stamina = stamina
        self.weapon_collection = weapon_collection
        self.health = health

    def __str__(self):
        return f"\n'Character Name': {self.name}, \n'Current Location': {self.location}, \n'Stamina': {self.stamina}, \n'Weapons Available': {self.weapon_collection}, \n'Health': {self.health} "

