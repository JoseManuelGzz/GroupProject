from Dataset import Dataset
from ObjectiveFunction import MinimisingFunction
from ObjectiveFunction import MaximisingFunction
from Mutator import Mutator
from SAAlgorithm_Draft import SAAlgorithm
from Status import Status
from Solution import Solution

columns = 10

rows = 5

max_iterations = 100

alphabet=range(0,4)

alpha = 0.95

initial_c = 200

status = Status(max_iterations, rows, columns, len(alphabet))

dataset = Dataset(rows= rows, cols = columns, alphabet=alphabet)


data = dataset.get_data()

mutator = Mutator(dataset)

solution = Solution(dataset)

solution_data = solution.get_solution()

"""
print(solution_data)
x = mutator.use_random_flip_2(solution_data, 0.3)
print(x)
"""

min_obj_f = MinimisingFunction()
max_obj_f = MaximisingFunction(3)


#def _init_(self, dataset, solution, mutator, obj_func):


sa = SAAlgorithm(data, solution_data, mutator, min_obj_f, status)

status = sa.run(alpha, initial_c)

print(status.get_solution_record())






