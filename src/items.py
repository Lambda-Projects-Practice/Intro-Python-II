class Items:
    def __init__(self, weapon_name = 'sword', power = 5):
        self.weapon_name = weapon_name
        self.power = power

    def __str__(self):
        return f"Weapon Name: {self.weapon_name}, \nPower of Weapon: {self.power} "