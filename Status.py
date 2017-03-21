"""
Status: Class to keep track of performance of the
        different executions of the heurisitic
        algorithms
"""

import csv
class Status:
        """
        __init__
                Constructor for the Status class. The counters to
                keep track of the parameters in an algorithm simulation
                run.
                parameters:
                        max_iter - Maximum number of iterations
                        num_sequences - number of sequences in the dataset
                        sequence_length - number of characters in each sequence
                        alphabet_size - number of possible characters in the sequences
                returns:
                        -None-

        """
        def __init__(self, max_iter, num_sequences, sequence_length, alphabet_size):
                self.max_iter = max_iter
                self.num_sequences = num_sequences
                self.sequence_length = sequence_length
                self.alphabet_size = alphabet_size
                self.num_iter = 0
                self.func_calls = 0
                self.func_evaluation = []
                self.elapsed_time = 0.0
                self.sa_parameters = {'c': [], 'alpha': 0}
                self.ga_parameters = {}
                self.mcm_parameters = {}
                self.re_parameters = {}
                self.solution_record = []
                self.best_solution = []

        """
        add_iteration
                Add one iteration to the object's counter for iterations
                parameters:
                        -NA- 
                returns:
                        -NA-

        """
        def add_iteration(self):
                self.num_iter = self.num_iter + 1

        """
        add_function_calls
                Add one function call to the object's counter
                parameters:
                        -NA-
                returns:
                        -NA-

        """
        def add_function_calls(self):
                self.func_calls = self.func_calls + 1

        """
        add_function_evaluation
                Add a new evaluation of the functionto the object's counter, 
                        which represents the quality of the current proposed solution 
                        at a given iteration
                parameters:
                        func_value - number representing the objective function
                                evaluation
                returns:
                        -NA-
                        
        """
        def add_function_evaluation(self, func_value):
                self.func_evaluation.append(func_value)

        """
        add_c_sa_parameters
                Keep track of the temperature parameter, useful for the 
                        Simulated Annealing Algorithm simulation
                parameters:
                        c_value - temperature value given by the user to
                                keep track
                returns:
                        -NA-

        """
        def add_c_sa_parameters(self, c_value):
                self.sa_parameters["c"].append(c_value)

        """
        add_solution_record_entry
                Add an entry to the collection of lists that represent
                        the behaviour of a simulation across its multiple iterations
                parameters:
                        entry - a list with standard values representing the current
                                iteration, the number of function calls, the best evaluation
                                so far and the current evaluation
                returns:
                        -NA-

        """
        def add_solution_record_entry(self, entry):
                self.solution_record.append(entry)

        """
        set_alpha_value_sa
                Update the alpha parameter for the Simulated Annealing simulations
                parameters:
                        alpha - numeric value representing the alpha to be used 
                returns:
                        -NA-

        """
        def set_alpha_value_sa(self, alpha):
                self.sa_parameters['alpha'] = alpha

        """
        set_elapsed_time
                Function that enables the user to keep track of the time
                        that an algorithm takes to run completely
                parameters:
                        elapsed_time - numeric value representing the number of
                                elapsed from start to finish 
                returns:
                        -NA-

        """
        def set_elapsed_time(self, elapsed_time):
                self.elapsed_time = elapsed_time

        """
        get_function_calls
                retrieve the number of cuntion calls  in the current status object
                parameters:
                        -NA- 
                returns:
                        The number that represents how many times the objective
                                function was called

        """
        def get_function_calls(self):
                return self.func_calls

        """
        get_max_iterations
                Function to retrieve the store number of max iterations
                parameters:
                        -NA-
                returns:
                        Numeric value representing the maximum iterations set 
                        on the object

        """
        def get_max_iterations(self):
                return self.max_iter

        """
        get_solution_record
                Retrieve the attribute of the object thar stores the information
                        about the simulation run
                parameters:
                        -NA- 
                returns:
                        A list of lists with the information about an algorithm run

        """
        def get_solution_record(self):
                return self.solution_record

        """
        save_to_file
                Function that enables the user to save the solution_record entries
                        to a csv file
                parameters:
                        file_name - String with the path for the file to be created
                returns:
                        -NA-

        """
        def save_to_file(self, file_name):
                with open(file_name, "wb") as out_file:
                        csv_obj = csv.writer(out_file)
                        csv_obj.writerows(self.solution_record)

        """
        load_from_file
                Function that enables a user to load a solution_record from a 
                CSV file
                parameters:
                        file_name - String with the path for the file to be loaded 
                returns:
                        -NA-
        """
        def load_from_file(self, file_name):
                result = []
                with open(file_name, "rb") as in_file:
                        file_reader = csv.reader(in_file, delimiter=',')
                        for row in file_reader:
                                result.append(row)
                self.solution_record = result

        """
        set_best_solution
                Function tha enables the user to save the best list of characters
                        that represent a solution to an instance of a String Consensus
                        Algorithm
                parameters:
                        solution - list containing a sequence of characters with the best solution 
                returns:
                        -NA-
        """
        def set_best_solution(self, solution):
                self.best_solution = solution

        """
        get_best_solution
                Function that enables the user to retrieve the best solution stored for 
                        a given instance of a String Consenus Problem simulation
                parameters:
                        -NA-
                returns:
                        the list containing the best solution
        """
        def get_best_solution(self):
                return self.best_solution
