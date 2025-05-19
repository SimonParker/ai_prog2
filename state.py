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


#returns a new generation filled with new individuals, the same number as in the old generation
def repopulate(generation, mutation_chance):
  new_gen = []
  for i in range(len(generation) // 2):
    parents = randomly_sample(generation) #parents can be the same
    c1, c2 = crossover(parents[0], parents[1])
    c1.mutate(mutation_chance)
    c2.mutate(mutation_chance)
    new_gen.append((c1, heuristic(c1)))
    new_gen.append((c2, heuristic(c2)))
  return new_gen


def randomly_sample(generation):
  individuals = [x[0] for x in generation]
  fitnesses = [x[1] for x in generation]
  return random.choices(individuals, weights=fitnesses, k=2)

#this returns 1 child. randomly choose 1 of the results from the crossover
def crossover(p1, p2):
  child = []
  cross_point = random.randint(1, 7)
  return State(p1.state[:cross_point] + p2.state[cross_point:]), State(p2.state[:cross_point] + p1.state[cross_point:])


#the number of non-attacking pairs of queens, see slides
def heuristic(board):
  score = 0
  pos = [0, 1, 2, 3, 4, 5, 6, 7]
  pairs = [(pos[x], pos[y]) for x in range(len(pos)) for y in range(x + 1, len(pos))]
  for x, y in pairs:
    if board.state[x] == board.state[y] or abs(board.state[y] - board.state[x]) == y - x:
      score += 1
  return 28 - score


class State():
  def __init__(self, state):
    self.state = state #state is a len 8 list of integers, 1-8, that describe which row the queen in that column is in

  def __str__(self):
    return f"{self.state}"

  def __repr__(self):
    return f"{self.state}"

  def mutate(self, chance):
    for i in range(len(self.state)):
      roll = random.random() 
      if roll < chance:
        self.state[i] = random.randint(1, 8) #genes can mutate into themselves




