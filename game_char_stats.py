class GameCharacter:
    def __init__(self , name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self , _health):
        if _health < 0:
            self._health = 0
        elif _health >100:
            self._health = 100
        else:
            self._health = _health
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self , _mana):
        if _mana <0:
            self._mana = 0
        elif _mana >50:
            self._mana =50
        else:
            self._mana = _mana
    
    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level +=1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")
    

    def __str__(self):
        line = ''
        line += f"Name: {self.name}\n"
        line += f"Level: {self.level}\n"
        line += f"Health: {self.health}\n"
        line += f"Mana: {self.mana}"
        return line


##This part is code testing
hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up