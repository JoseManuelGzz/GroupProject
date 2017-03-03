from Dataset import Dataset
from ObjectiveFunction import ObjectiveFunction
from Mutator import Mutator
from SAAlgorithm_Draft import SAAlgorithm
from Status import Status
from Solution import Solution

columns = 3

dataset = Dataset(rows=10,cols = columns)

data = dataset.get_data()

mutator = Mutator()

obj = ObjectiveFunction()

sa = SAAlgorithm()

status = Status(100)

solution = Solution(cols = columns)






