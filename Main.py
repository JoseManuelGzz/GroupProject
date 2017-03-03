from Dataset import Dataset
from ObjectiveFunction import MinimisingFunction
from ObjectiveFunction import MaximisingFunction
from Mutator import Mutator
from SAAlgorithm_Draft import SAAlgorithm
from Status import Status
from Solution import Solution

columns = 3

dataset = Dataset(rows=10,cols = columns)

data = dataset.get_data()

mutator = Mutator()

min_obj_f = MinimisingFunction()
max_obj_f = MaximisingFunction(3)

solution = Solution(cols = columns)
solution_data = solution.get_solution()

status = Status(100)

#def _init_(self, dataset, solution, mutator, obj_func):


sa = SAAlgorithm(data, solution_data, mutator, min_obj_f)

sa.run()







