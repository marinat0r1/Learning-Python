class Marin:
    def __init__(self, strength, live):
        self.name = "Marin"
        self.age = 21
        self.strength = strength
        self.live = live

    def stronger(self, additionalStrength):
        self.strength += additionalStrength
    
    def dealDemage(self):
        return self.strength

    def takeDemage(self, demage):
        self.live -= demage


m1 = Marin(95, 300)
m1.stronger(15)
print("Name: ", m1.name, "Age: ", m1.age, "Strength: ", m1.strength)

class WeakMarin(Marin):
    def __init__(self):
        super().__init__(5, 100)
        self.name = "Weak Marin"

m2 = WeakMarin()
m2.stronger
print("Name: ", m2.name, "Age: ", m2.age, "Strength: ", m2.strength)

class StrongMarin(Marin):
    def __init__(self):
        super().__init__(999, 2000)
        self.name = "Weak Marin"

m3 = StrongMarin()
m3.stronger
print("Name: ", m3.name, "Age: ", m3.age, "Strength: ",m3.strength)

class BattleManager:

    def fight(self, player1, player2):
        while player1.live > 0 and player2.live > 0:
            player2.takeDemage(player1.strength)
            print("Player 1 hit em...Player2 now down to ", player2.live, "points")
            player1.takeDemage(player2.strength)
            print("Player 2 hit em...Player1 now down to ", player1.live, "points")
        if player1.live > 0:
            print("Player1 won this battle!")
        else:
            print("Player2 won this battle")

conquerersStrength = int(input("Player1! How strong are you? "))
cunquerersLive = int(input("Player1! How much live do you have? "))
print("\n")
avangersStrength = int(input("Player2! How strong are you? "))
avangersLive = int(input("Player2! How much live do you have? "))
print("\n")
theConquerer = Marin(conquerersStrength, cunquerersLive)
theAvanger = Marin(avangersStrength, avangersLive)
battle1 = BattleManager()
battle1.fight(theConquerer,theAvanger)

