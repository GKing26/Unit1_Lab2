from random import choice
class Rat:
  def __init__(self, sex, weight):
    self.sex = sex
    self.litters = 0
    self.weight = weight
    self.name = choice(["Doggy", "Eggbeater","Potat Mc Fries","Remmi","Bayblade","Turtle","Bipples","Yurgie","Mop","Saltine","Brick"])
  def mutater(self,mutationAmount):
    self.weight *= mutationAmount

  def getWeight(self):
    return self.weight
  def getSex(self):
    return self.sex
  def canBreed(self):
    return self.litters <= 5
  def __str__(self):
    return f"\n  Name: {self.name}\n  Sex: {self.sex}\n  Grams: {int(self.weight)}"
  def __repr__(self):
    return f"{self.sex} - {self.weight}"

  def __lt__(self,other):
    return self.weight < other.weight
  def __gt__(self,other):
    return self.weight > other.weight
  def __le__(self,other):
    return self.weight <= other.weight
  def __ge__(self,other):
    return self.weight >= other.weight
  def __eq__(self,other):
    return self.weight == other.weight