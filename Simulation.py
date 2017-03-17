from Dataset import Dataset
from ObjectiveFunction import CSPObjectiveFunction
from ObjectiveFunction import FFMSPObjectiveFunction
from Mutator import Mutator
from SAAlgorithm_Draft import SAAlgorithm
from Montecarlo import Montecarlo
from Status import Status
from Solution import Solution
from Figures import Figure
"""
<class name>: <class description/objective>
        (?)<subclass name>: <subclass description/objective>
"""
class Simulation:

	def __init__(self, algorithm, columns, rows, max_iterations, alphabet, alpha, initial_c):
		self.algorithm = algorithm
		self.status = status
        self.columns = columns
        self.rows = rows
        self.max_iterations = max_iterations
        self.alphabet = alphabet
        self.alpha = alpha
        self.initial_c = initial_c
        self.status = Status(max_iterations, rows, columns, len(alphabet))
        dataset = Dataset(rows= rows, cols = columns, alphabet=alphabet)
        data = dataset.get_data()
        mutator = Mutator(dataset)
        solution = Solution(dataset)
        solution_data = solution.get_solution('csp')
        min_obj_f = CSPObjectiveFunction()
        max_obj_f = FFMSPObjectiveFunction(0.75 * columns)
        sa = Montecarlo(data, solution_data, mutator, min_obj_f, status)
        status = sa.run(alpha, initial_c)
        status.save_to_file('csp_run.csv')

	"""
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

    """
	def get_solution():
		algorithm.run_problem(algorithm, status)

