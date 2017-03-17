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

	def __init__(self, columns, rows, max_iterations, alphabet, problem_type, threshold_proportion=0.75):
		self.status = status
        self.columns = columns
        self.rows = rows
        self.max_iterations = max_iterations
        self.alphabet = alphabet
        self.status = Status(max_iterations, rows, columns, len(alphabet))
        self.dataset = Dataset(rows= rows, cols = columns, alphabet=alphabet)
        self.data = dataset.get_data()
        self.mutator = Mutator(dataset)
        self.solution = Solution(dataset)
        self.solution_data = solution.get_solution(problem_type)

	"""
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

    """
	#def get_solution():
		#algorithm.run_problem(algorithm, status)
        #Create figures in here

class simulationSA_CSP(Simulation):
    def __init__(self, alpha, initial_c):
        self.alpha = alpha
        self.initial_c = initial_c
        self.min_obj_f = CSPObjectiveFunction()
        self.simulated_annealing = SAAlgorithm(self.data, self.solution_data, self.mutator, self.min_obj_f, self.status)    

    def get_solution():
        self.status = simulated_annealing.run(self.alpha, self.initial_c)
        self.status.save_to_file('sa_csp_run.csv')

class simulationSA_FFMSP(Simulation):
    def __init__(self, alpha, initial_c):
        self.alpha = alpha
        self.initial_c = initial_c
        self.max_obj_f = FFMSPObjectiveFunction(self.threshold_proportion * self.columns)
        self.simulated_annealing = SAAlgorithm(self.data, self.solution_data, self.mutator, self.max_obj_f, self.status)

    def get_solution():
        self.status = simulated_annealing.run(self.alpha, self.initial_c)
        self.status.save_to_file('sa_ffmsp_run.csv')

class simulationMCM(Simulation):

class simulationGA(Simulation):

class simulationEv(Simulation):
        

