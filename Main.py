from Dataset import Dataset
from ObjectiveFunction import MinimisingFunction
from ObjectiveFunction import MaximisingFunction
from Mutator import Mutator
from SAAlgorithm_Draft import SAAlgorithm
from Status import Status
from Solution import Solution

columns = 10

dataset = Dataset(rows=5,cols = columns, alphabet=range(0,4))

data = dataset.get_data()

mutator = Mutator(dataset)

solution = Solution(dataset)
solution_data = solution.get_solution()

print(solution_data)
x = mutator.use_random_flip_2(solution_data, 0.3)
print(x)

"""

min_obj_f = MinimisingFunction()
max_obj_f = MaximisingFunction(3)


status = Status(100)

#def _init_(self, dataset, solution, mutator, obj_func):


sa = SAAlgorithm(data, solution_data, mutator, min_obj_f)

sa.run()
"""






