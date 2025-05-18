#simon parker
from state import *

generation = []
for i in range(5):
  generation.append((rand_board(), i))

print(generation)
print(evaluate(generation))
print(best_individual(generation))
