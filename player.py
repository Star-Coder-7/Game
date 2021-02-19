class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _getLives(self):
        return self._lives

    def _setLives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative.")
            self._lives = 0

    lives = property(_getLives, _setLives)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, levels):
        if levels >= 1:
            # delta = levels - self._level
            # self.score += delta * 1000
            # self._level = levels
            self._level = levels
            self._score = (self._level - 1) * 1000
        else:
            print("Level cannot be less than 1")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self._level}, Score: {self._score}"



