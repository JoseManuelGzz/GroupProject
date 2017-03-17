from Dataset import Dataset
from ObjectiveFunction import CSPObjectiveFunction
from ObjectiveFunction import FFMSPObjectiveFunction
from Mutator import Mutator
from SAAlgorithm_Draft import SAAlgorithm
from Montecarlo import Montecarlo
from Status import Status
from Solution import Solution
#from Figures import Figure  
"""

<class name>: <class description/objective>

"""
class Simulation:
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion):
        self.columns = columns
        self.rows = rows
        self.max_iterations = max_iterations
        self.alphabet = alphabet
        self.status = Status(max_iterations, rows, columns, len(alphabet))
        self.dataset = Dataset(rows= rows, cols = columns, alphabet=alphabet)
        self.data = self.dataset.get_data()
        self.mutator = Mutator(self.dataset)

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

"""

<class name>: <class description/objective>

"""
class SimulationSA_CSP(Simulation):
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, alpha, initial_c):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion)
        self.alpha = alpha
        self.initial_c = initial_c
        self.min_obj_f = CSPObjectiveFunction()
        self.solution = Solution(self.dataset)
        self.solution_data = self.solution.get_solution('csp')   
        self.simulated_annealing = SAAlgorithm(self.data, self.solution_data, self.mutator, self.min_obj_f, self.status) 

    def get_solution(self):
        self.status = self.simulated_annealing.run(self.alpha, self.initial_c)
        self.status.save_to_file('sa_csp_run.csv')

"""

<class name>: <class description/objective>

"""
class SimulationSA_FFMSP(Simulation):
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, alpha, initial_c):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion)
        self.alpha = alpha
        self.initial_c = initial_c
        self.max_obj_f = FFMSPObjectiveFunction(threshold_proportion * self.columns)
        self.solution = Solution(self.dataset)
        self.solution_data = self.solution.get_solution('ffmsp')   
        self.simulated_annealing = SAAlgorithm(self.data, self.solution_data, self.mutator, self.max_obj_f, self.status)

    def get_solution(self):
        self.status = self.simulated_annealing.run(self.alpha, self.initial_c)
        self.status.save_to_file('sa_ffmsp_run.csv')

"""

<class name>: <class description/objective>

"""
class SimulationMCM(Simulation):
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion)

"""

<class name>: <class description/objective>

"""
class SimulationGA(Simulation):
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion)    

"""

<class name>: <class description/objective>

"""
class SimulationEv(Simulation):
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, number_children):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion)


