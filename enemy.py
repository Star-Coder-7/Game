from random import randint


class Enemy:

    def __init__(self, name='Enemy', hitPoints=0, lives=1, maxHitPoints=0):
        self._name = name
        self._hitPoints = hitPoints
        self._lives = lives
        self._maxHitPoints = 0
        self._alive = True

    def takeDamage(self, damage):
        remainingPoints = self._hitPoints - damage

        if remainingPoints >= 0:
            self._hitPoints = remainingPoints
            print(f"{self._name} took {damage} points of damage and has {self._hitPoints} hit points left.")

        else:
            self._lives -= 1
            self._hitPoints = 0
            self._hitPoints = self._maxHitPoints
            print(f"{self._name} took {damage} points of damage and has {self._hitPoints} hit points left.")

            if self._lives <= 0:
                print(f"{self._name} has successfully been defeated!!!")
                self.alive = False

            else:
                print(f"{self._lives} lost a life!!!")
                self._alive = True

    def regenerate(self, bonus):
        if randint(1, 2) == 1:
            bonus = randint(1, 3)
            self._lives += bonus
        else:
            bonus = randint(1, 3)
            self._hitPoints += bonus
            self._maxHitPoints += bonus

    def __str__(self):
        return f"Name: {self._name}, Lives: {self._lives}, Hit points: {self._hitPoints}"


class Troll(Enemy):

    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hitPoints=23)
        super().__init__(name=name, lives=1, hitPoints=23)   # To call the super class Enemy

    def grunt(self):
        print(f"Me {self._name}. {self._name} grunt at you!!!")

    def stomp(self):
        print(f"Me {self._name}. {self._name} stomp on the ground fiercely!!!")
        
    def defend(self):
        if randint(1, 3) == 2:
            print(f"{self._name} defended thyself!")

    def takeDamage(self, damage):
        if not self.defend():
            super().takeDamage(damage=damage)

    def regenerate(self, bonus):
        if self.defend() and randint(1, 2) == 2:
            super().regenerate(bonus=bonus)


class TrollKing(Troll):

    def __init__(self, name):
        super().__init__(name=name)
        self._lives = 5
        self._hitPoints = 50
        self._maxHitPoints = 50

    @staticmethod
    def grunt():
        super().grunt()

    @staticmethod
    def stomp():
        super().stomp()

    @staticmethod
    def defend():
        super().defend()

    @staticmethod
    def takeDamage(damage):
        super().takeDamage(damage=damage)

    @staticmethod
    def regenerate(bonus):
        super().regenerate(bonus=bonus)


class TrollQueen(Troll):

    def __init__(self, name):
        super().__init__(name=name)
        self._lives = 8
        self._hitPoints = 45
        self._maxHitPoints = 45

    @staticmethod
    def grunt():
        super().grunt()

    @staticmethod
    def stomp():
        super().stomp()

    @staticmethod
    def defend():
        super().defend()

    @staticmethod
    def takeDamage(damage):
        super().takeDamage(damage=damage)

    @staticmethod
    def regenerate(bonus):
        super().regenerate(bonus=bonus)


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hitPoints=38)

    def scary(self):
        print(f"{self._name} is I. {self._name} will scare you!!!")

    def transform(self):
        print(f"(Screech) Now me, {self._name} is a bat!!!")

    def defend(self):
        if randint(1, 3) == 3:
            print(f"{self._name} defended thyself!")

    def takeDamage(self, damage):
        if not self.defend():
            super().takeDamage(damage=damage)

    def regenerate(self, bonus):
        if randint(1, 2) == 1:
            super().regenerate(bonus=bonus)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._lives = 10
        self._hitPoints = 75
        self._maxHitPoints = 75

    @staticmethod
    def scary():
        super().scary()

    @staticmethod
    def transform():
        super().transform()

    @staticmethod
    def defend():
        super().defend()

    @staticmethod
    def takeDamage(damage):
        super().takeDamage(damage=damage)

    @staticmethod
    def regenerate(bonus):
        super().regenerate(bonus=bonus)


class VampireQueen(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._lives = 8
        self._hitPoints = 80
        self._maxHitPoints = 80

    @staticmethod
    def scary():
        super().scary()

    @staticmethod
    def transform():
        super().transform()

    @staticmethod
    def defend():
        super().defend()

    @staticmethod
    def takeDamage(damage):
        super().takeDamage(damage=damage)

    @staticmethod
    def regenerate(bonus):
        super().regenerate(bonus=bonus)