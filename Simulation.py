from Dataset import Dataset
from ObjectiveFunction import CSPObjectiveFunction
from ObjectiveFunction import FFMSPObjectiveFunction
from Mutators_v2 import ExpMutator
from Mutators_v2 import RandomFlip
from SimulatedAnnealing import SAAlgorithm
from GAlgorithm import GAlgorithm
from Montecarlo import Montecarlo
from Status import Status
from Solution import Solution
from Evolutionary import Evolutionary
from Figures import Figure  

"""

<Simulation>: <This class serves as the main constructor for simulating 
                all of the algorithms in the package. It provides a 
                constructor for Simulated Annealing, Monte Carlo Metropolis,
                a Genetic Algorithm, and an Evolutionary Algorithm. Each 
                has a constructor for CSP and FFMSP.>

"""
class Simulation:
    """
    <__init__>
            <Constructor of the Simulation class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function
                    <mutator_name> - Name of the mutator to be used        
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name):
        self.columns = columns
        self.rows = rows
        self.max_iterations = max_iterations
        self.alphabet = alphabet
        self.status = Status(max_iterations, rows, columns, len(alphabet))
        self.dataset = Dataset(rows= rows, cols = columns, alphabet=alphabet)
        self.data = self.dataset.get_data()
        if mutator_name == 'RandomFlip':
            self.mutator = RandomFlip(self.dataset, 0.3)
        elif mutator_name == 'Exponential':
            self.mutator = ExpMutator(self.dataset, 0.3)

"""

<SimulationSA_CSP>: <This class is used to create an instance and get the solution
                    for the CSP using the Simulated Annealing algorithm. It inherits 
                    attributes from the Simulation Class>

"""
class SimulationSA_CSP(Simulation):
    """
    <__init__>
            <Constructor of the SimulationSA_CSP class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function  
                    <mutator_name> - Name of the mutator to be used
                    <alpha> - Cooling value for the temperature 
                    <initial_c> - Temperature value        
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name, alpha, initial_c):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name)
        self.alpha = alpha
        self.initial_c = initial_c
        self.min_obj_f = CSPObjectiveFunction()
        self.solution = Solution(self.dataset)
        self.solution_data = self.solution.get_solution('csp')   
        self.simulated_annealing = SAAlgorithm(self.data, self.solution_data, self.mutator, self.min_obj_f, self.status) 
    """
    <get_solution>
            <Function that runs the Simulated Annealing algorithm for the CSP
            and stores the results in the Status attribute>
            parameters:
                    <self> - Pointer to the object    
            returns:
                    -NA-
    """
    def get_solution(self):
        self.status = self.simulated_annealing.run(self.alpha, self.initial_c)
        self.status.save_to_file('sa_csp_run.csv')

"""

<SimulationSA_FFMSP>: <This class is used to create an instance and get the solution
                    for the FFMSP using the Simulated Annealing algorithm. It inherits 
                    attributes from the Simulation Class>

"""
class SimulationSA_FFMSP(Simulation):
    """
    <__init__>
            <Constructor of the SimulationSA_FFMSP class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function  
                    <mutator_name> - Name of the mutator to be used
                    <alpha> - Cooling value for the temperature 
                    <initial_c> - Temperature value        
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name, alpha, initial_c):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name)
        self.alpha = alpha
        self.initial_c = initial_c
        self.max_obj_f = FFMSPObjectiveFunction(threshold_proportion * self.columns)
        self.solution = Solution(self.dataset)
        self.solution_data = self.solution.get_solution('ffmsp')   
        self.simulated_annealing = SAAlgorithm(self.data, self.solution_data, self.mutator, self.max_obj_f, self.status)
    """
    <get_solution>
            <Function that runs the Simulated Annealing algorithm for the FFMSP
            and stores the results in the Status attribute>
            parameters:
                    <self> - Pointer to the object    
            returns:
                    -NA-
    """
    def get_solution(self):
        self.status = self.simulated_annealing.run(self.alpha, self.initial_c)
        self.status.save_to_file('sa_ffmsp_run.csv')

"""

<SimulationMCM_CSP>: <This class is used to create an instance and get the solution
                    for the CSP using the Monte Carlo Metropolis algorithm. It inherits 
                    attributes from the Simulation Class>

"""
class SimulationMCM_CSP(Simulation):
    """
    <__init__>
            <Constructor of the SimulationMCM_CSP class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function  
                    <mutator_name> - Name of the mutator to be used
                    <alpha> - Cooling value for the temperature 
                    <initial_c> - Temperature value        
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name, alpha, initial_c):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name)
        self.alpha = alpha
        self.initial_c = initial_c
        self.min_obj_f = CSPObjectiveFunction()
        self.solution = Solution(self.dataset)
        self.solution_data = self.solution.get_solution('csp')   
        self.montecarlo_metropolis = Montecarlo(self.data, self.solution_data, self.mutator, self.min_obj_f, self.status)
    """
    <get_solution>
            <Function that runs the Monte Carlo Metropolis algorithm for the CSP
            and stores the results in the Status attribute>
            parameters:
                    <self> - Pointer to the object    
            returns:
                    -NA-
    """
    def get_solution(self):
        self.status = self.montecarlo_metropolis.run(self.alpha, self.initial_c)
        self.status.save_to_file('mcm_csp_run.csv')

"""

<SimulationMCM_FFMSP>: <This class is used to create an instance and get the solution
                    for the FFMSP using the Monte Carlo Metropolis algorithm. It inherits 
                    attributes from the Simulation Class>

"""
class SimulationMCM_FFMSP(Simulation):
    """
    <__init__>
            <Constructor of the SimulationMCM_FFMSP class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function  
                    <mutator_name> - Name of the mutator to be used
                    <alpha> - Cooling value for the temperature
                    <initial_c> - Temperature value        
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name, alpha, initial_c):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name)
        self.alpha = alpha
        self.initial_c = initial_c
        self.max_obj_f = FFMSPObjectiveFunction(threshold_proportion * self.columns)
        self.solution = Solution(self.dataset)
        self.solution_data = self.solution.get_solution('ffmsp')   
        self.montecarlo_metropolis = Montecarlo(self.data, self.solution_data, self.mutator, self.max_obj_f, self.status)
    """
    <get_solution>
            <Function that runs the Monte Carlo Metropolis algorithm for the FFMSP
            and stores the results in the Status attribute>
            parameters:
                    <self> - Pointer to the object    
            returns:
                    -NA-
    """
    def get_solution(self):
        self.status = self.montecarlo_metropolis.run(self.alpha, self.initial_c)
        self.status.save_to_file('mcm_ffmsp_run.csv')
"""

<SimulationGA_CSP>: <This class is used to create an instance and get the solution
                    for the CSP using the Genetic algorithm. It inherits attributes 
                    from the Simulation Class>

"""
class SimulationGA_CSP(Simulation):
    """
    <__init__>
            <Constructor of the SimulationGA_CSP class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function  
                    <mutator_name> - Name of the mutator to be used    
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name)    
        self.min_obj_f = CSPObjectiveFunction()
        self.solution = Solution(self.dataset)
        self.solution_data = self.solution.get_solutions(self.rows)
        self.genetic_algorithm = GAlgorithm(self.data, self.solution_data, self.mutator, self.min_obj_f, self.status)
    """
    <get_solution>
            <Function that runs the Genetic algorithm for the CSP
            and stores the results in the Status attribute>
            parameters:
                    <self> - Pointer to the object    
            returns:
                    -NA-
    """
    def get_solution(self):
        self.status = self.genetic_algorithm.run(self.max_iterations, 0.3)
        self.status.save_to_file('ga_csp_run.csv')
"""

<SimulationGA_FFMSP>: <This class is used to create an instance and get the solution
                    for the FFMSP using the Genetic algorithm. It inherits attributes 
                    from the Simulation Class>

"""
class SimulationGA_FFMSP(Simulation):
    """
    <__init__>
            <Constructor of the SimulationGAFFMSP class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function  
                    <mutator_name> - Name of the mutator to be used  
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name)  
        self.max_obj_f = FFMSPObjectiveFunction(threshold_proportion * self.columns)
        self.solution = Solution(self.dataset)
        self.solution_data = self.solution.get_solutions(self.rows)
        self.genetic_algorithm = GAlgorithm(self.data, self.solution_data, self.mutator, self.max_obj_f, self.status)
    """
    <get_solution>
            <Function that runs the Genetic algorithm for the FFMSP
            and stores the results in the Status attribute>
            parameters:
                    <self> - Pointer to the object    
            returns:
                    -NA-
    """
    def get_solution(self):
        self.status = self.genetic_algorithm.run(self.max_iterations, 0.3)
        self.status.save_to_file('ga_ffmsp_run.csv')
"""

<SimulationEv_CSP>: <This class is used to create an instance and get the solution
                    for the CSP using the Evolutionary algorithm. It inherits attributes 
                    from the Simulation Class>

"""
class SimulationEv_CSP(Simulation):
    """
    <__init__>
            <Constructor of the SimulationEv_CSP class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function   
                    <mutator_name> - Name of the mutator to be used
                    <number_parents> - Number of parents for each element
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name, number_parents):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name)
        self.min_obj_f = CSPObjectiveFunction()
        self.solution = Solution(self.dataset)
        self.evolutionary = Evolutionary(dataset=self.dataset, mutator=self.mutator, solution=self.solution, obj_func=self.min_obj_f, num_parents=number_parents, status=self.status )
    """
    <get_solution>
            <Function that runs the Evolutionary algorithm for the CSP
            and stores the results in the Status attribute>
            parameters:
                    <self> - Pointer to the object    
            returns:
                    -NA-
    """
    def get_solution(self):
        self.status = self.evolutionary.run()
        self.status.save_to_file('evo_csp_run.csv')
"""

<SimulationEv_FFMSP>: <This class is used to create an instance and get the solution
                    for the FFMSP using the Evolutionary algorithm. It inherits attributes 
                    from the Simulation Class>

"""
class SimulationEv_FFMSP(Simulation):
    """
    <__init__>
            <Constructor of the SimulationEv_FFMSP class>
            parameters:
                    <self> - Pointer to the object
                    <columns> - Number of columns in the dataset
                    <rows> - Number of rows in the dataset
                    <max_iterations> - Maximum number of iterations to run the algorithm
                    <alphabet> - Range of characters for the sequences
                    <threshold_proportion> - Constant used for the FFMSP objective function   
                    <mutator_name> - Name of the mutator to be used
                    <number_parents> - Number of parents for each element
            returns:
                    -NA-
    """
    def __init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name, number_parents):
        Simulation.__init__(self, columns, rows, max_iterations, alphabet, threshold_proportion, mutator_name)
        self.max_obj_f = FFMSPObjectiveFunction(threshold_proportion * self.columns)
        self.solution = Solution(self.dataset)
        self.evolutionary = Evolutionary(dataset=self.dataset, mutator=self.mutator, solution=self.solution,
                                         obj_func=self.max_obj_f, num_parents=number_parents, status=self.status)
    """
    <get_solution>
            <Function that runs the Evolutionary algorithm for the FFMSP
            and stores the results in the Status attribute>
            parameters:
                    <self> - Pointer to the object    
            returns:
                    -NA-
    """
    def get_solution(self):     
        self.status = self.evolutionary.run()
        self.status.save_to_file('evo_ffmsp_run.csv')