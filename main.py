# Griffin King
# U1 Lab 1
# Making a large rat population
from Ratatoullie import Rat
from random import triangular
from random import choice
from random import randint 
from random import uniform
import time
GOAL = 50000                # Target average weight (grams)
NUM_RATS = 20               # Max adult rats in the lab
INITIAL_MIN_WT = 200        # The smallest rat (grams)
INITIAL_MAX_WT = 600        # The chonkiest rat (grams)
INITIAL_MODE_WT = 300       # The most common weight (grams)
MUTATE_ODDS = 0.01          # Liklihood of a mutation
MUTATE_MIN = 0.5            # Scalar mutation - least beneficial
MUTATE_MAX = 1.2            # Scalar mutation - most beneficial
LITTER_SIZE = 8             # Pups per litter (1 mating pair)
GENERATIONS_PER_YEAR = 10   # How many generations are created each year
GENERATION_LIMIT = 500      # Generational cutoff - stop breeded no matter what
def initial_population():
  '''Create the initial set of rats based on constants'''
  rats = [[],[]]
  mother = Rat("F", INITIAL_MIN_WT)
  father = Rat("M", INITIAL_MAX_WT)
  
  for r in range(NUM_RATS):
    if r < 10:
      sex = "M"
      ind = 0
    else:
      sex = "F"
      ind = 1
  
    wt = calculate_weight(sex, mother, father)
    R = Rat(sex, wt)
    rats[ind].append(R)
  
  return rats


def calculate_weight(sex, mother, father):
 
  min = mother.getWeight()
  max = father.getWeight()

  if sex == "M":
    wt = int(triangular(min, max, max))
  else:
    wt = int(triangular(min, max, min))
  return wt




def mutate(pups):
  for a in pups:
    for b in a:
      if randint(1,100) == 1:
        b.mutater(uniform(MUTATE_MIN,MUTATE_MAX))
  return pups  


def breed(rats):
  pups = [[],[]]

  for a in range(int(NUM_RATS/2)):
    for b in range(LITTER_SIZE):
      if b < 4:
        wt = calculate_weight("M", rats[0][a], rats[1][a])
        pups[0].append(Rat("M",wt))
      else:
        wt = calculate_weight("F", rats[0][a], rats[1][a])
        pups[1].append(Rat("F",wt))

  children = mutate(pups)
  return children  



def select(rats, pups, lost):
  all_rats = [rats[0]+pups[0],rats[1]+pups[1]]
  all_rats[0].sort(reverse=True)
  all_rats[1].sort(reverse=True)

  for a in all_rats:
    for b in a:
      if b.canBreed():
        pass
      else:
        a.remove(b)
        lost += 1

  rats = [all_rats[0][0:10],all_rats[1][0:10]]
  lost += 60

  if rats[0][0].__ge__(rats[1][0]):
    largest = rats[0][0]
  else:
    largest = rats[1][0]
  return rats, largest, lost


def calculate_mean(rats):
  sumWt = 0
  for a in rats:
    for b in a:
      sumWt += b.getWeight()
  return sumWt // NUM_RATS


def fitness(rats):
  mean = calculate_mean(rats)
  return mean >= GOAL, mean

def main():

  duration = time.time()
  lost = 0
  averages = [] 
  generations = 0
  funnyRatpic = ["  The rats have now formed a functional society, this one is an accountant","\n                       .____________.",
 "                       |Taxi Service|",
 "          (# )--(# )   ^-----||-----^",
 "          \\\  ()  ()_        ||      ",
 "           \\\---__$/\$       ||      ",
 "           _ /./ \.\_ @@@    ||      ",
 "          /  \ /:\ / \//     ||      ",
 "          \\\  \\\ //   |^     ||      ",
 "         .@@@.       ./      ||      ",
 "        _=___=_\___..-       ||      ",
 "        |_____||| ||         ||      ",
 "              @@@ @@@        ||      ",
 "<>--------------------------------------"]

  rats = initial_population()

  while generations <= GENERATION_LIMIT:

    pups = breed(rats)
    rats, largest, lost = select(rats,pups,lost)
    wanted_Weight, mean = fitness(rats)
    averages.append(str(int(mean)))
    generations += 1

    if wanted_Weight:
      print(f"\n\n<>--------------------------------------\n  Rats have reached desired weight\n\n  Time Elapsed: {time.time()- duration}\n  Years: {generations/10}\n  Generations: {generations}\n  Rats Executed For The Cause: {lost}\n\n  Largest Rat:\n {largest}\n\n  Averages: \n{', '.join(averages)}\n<>--------------------------------------\n\n")
      for a in funnyRatpic:
        print(a)
      break
if __name__ == "__main__":
  main()


                             

      
