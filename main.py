from enemy import Enemy, Troll, Vampire, TrollKing, VampireKing, TrollQueen, VampireQueen

uglyTroll = Troll("Pug")
print(f"Ugly Troll - {uglyTroll}")

anotherTroll = Troll("Ug")
print(f"Another Troll - {anotherTroll}")

brother = Troll("Urg")
print(f"Brother Troll - {brother}")

uglyTroll.grunt()
anotherTroll.grunt()
brother.grunt()

uglyTroll.stomp()
anotherTroll.stomp()
brother.stomp()

trollKing = TrollKing("Grump")
trollQueen = TrollQueen("Gurmp")

print(f"King of Trolls - {trollKing}")
print(f"Queen of Trolls - {trollQueen}")

vampire = Vampire("Vamp")
print(f"Basic Vampire - {vampire}")

vampire.scary()
vampire.transform()

vampKing = VampireKing("Dracula")
vampQueen = VampireQueen("Draclua")

print(f"King of Vampires - {vampKing}")
print(f"Queen of Vampires - {vampQueen}")

anotherTroll.takeDamage(5)
trollKing.takeDamage(2)
trollQueen.takeDamage(3)
vampire.takeDamage(4)
vampKing.takeDamage(6)
vampQueen.takeDamage(1)

anotherTroll.defend()
trollKing.defend()
trollQueen.defend()
vampire.defend()
vampKing.defend()
vampQueen.defend()

anotherTroll.regenerate(1)
trollKing.regenerate(6)
trollQueen.regenerate(4)
vampire.regenerate(3)
vampKing.regenerate(2)
vampQueen.regenerate(5)






