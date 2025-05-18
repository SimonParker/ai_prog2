#simon parker
import random


def evaluate(generation):
  best_fitness = 0
  total_fitness = 0
  for i in range(len(generation)):
    fitness = generation[i][1]
    total_fitness += fitness
    if fitness > best_fitness:
      best_fitness = fitness
  return total_fitness / len(generation), best_fitness


def best_individual(generation):
  best_individual = (None, 0)
  for i in range(len(generation)):
    if generation[i][1] > best_individual[1]:
      best_individual = generation[i]
  return best_individual[0]

def rand_board():
  return State([random.randint(1, 8) for x in range(8)])

class State():
  def __init__(self, state):
    self.state = state #state is a len 8 list of integers, 1-8, that describe which row the queen in that column is in

  def __str__(self):
    return f"{self.state}"

  def __repr__(self):
    return f"{self.state}"
