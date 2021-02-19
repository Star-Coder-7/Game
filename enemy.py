from random import randint


class Enemy:

    def __init__(self, name='Enemy', hitPoints=0, lives=1, maxHitPoints=0):
        self.name = name
        self.hitPoints = hitPoints
        self.lives = lives
        self.maxHitPoints = 0
        self.alive = True

    def takeDamage(self, damage):
        remainingPoints = self.hitPoints - damage

        if remainingPoints >= 0:
            self.hitPoints = remainingPoints
            print(f"{self.name} took {damage} points of damage and has {self.hitPoints} hit points left.")

        else:
            self.lives -= 1
            self.hitPoints = 0
            self.hitPoints = self.maxHitPoints
            print(f"{self.name} took {damage} points of damage and has {self.hitPoints} hit points left.")

            if self.lives <= 0:
                print(f"{self.name} has successfully been defeated!!!")
                self.alive = False

            else:
                print(f"{self.lives} lost a life!!!")
                self.alive = True

    def regenerate(self, bonus):
        if randint(1, 2) == 1:
            bonus = randint(1, 3)
            self.lives += bonus
        else:
            bonus = randint(1, 3)
            self.hitPoints += bonus
            self.maxHitPoints += bonus

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hitPoints}"


class Troll(Enemy):

    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hitPoints=23)
        super().__init__(name=name, lives=1, hitPoints=23)   # To call the super class Enemy

    def grunt(self):
        print(f"Me {self.name}. {self.name} grunt at you!!!")

    def stomp(self):
        print(f"Me {self.name}. {self.name} stomp on the ground fiercely!!!")
        
    def defend(self):
        if randint(1, 3) == 2:
            print(f"{self.name} defended thyself!")

    def takeDamage(self, damage):
        if not self.defend():
            super().takeDamage(damage=damage)

    def regenerate(self, bonus):
        if self.defend() and randint(1, 2) == 2:
            super().regenerate(bonus=bonus)


class TrollKing(Troll):

    def __init__(self, name):
        super().__init__(name=name)
        self.lives = 5
        self.hitPoints = 50
        self.maxHitPoints = 50

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
        self.lives = 8
        self.hitPoints = 45
        self.maxHitPoints = 45

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
        print(f"{self.name} is I. {self.name} will scare you!!!")

    def transform(self):
        print(f"(Screech) Now me, {self.name} is a bat!!!")

    def defend(self):
        if randint(1, 3) == 3:
            print(f"{self.name} defended thyself!")

    def takeDamage(self, damage):
        if not self.defend():
            super().takeDamage(damage=damage)

    def regenerate(self, bonus):
        if randint(1, 2) == 1:
            super().regenerate(bonus=bonus)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self.lives = 10
        self.hitPoints = 75
        self.maxHitPoints = 75

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
        self.lives = 8
        self.hitPoints = 80
        self.maxHitPoints = 80

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