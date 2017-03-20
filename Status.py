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

        """
        add_iteration
                Add one iteration to the object's counter for iterations
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def add_iteration(self):
                self.num_iter = self.num_iter + 1

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def add_function_calls(self):
                self.func_calls = self.func_calls + 1

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def add_function_evaluation(self, func_value):
                self.func_evaluation.append(func_value)

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def add_c_sa_parameters(self, c_value):
                self.sa_parameters["c"].append(c_value)

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def add_solution_record_entry(self, entry):
                self.solution_record.append(entry)

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def set_alpha_value_sa(self, alpha):
                self.sa_parameters['alpha'] = alpha

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def set_elapsed_time(self, elapsed_time):
                self.elapsed_time = elapsed_time

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def get_function_calls(self):
                return self.func_calls

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def get_max_iterations(self):
                return self.max_iter

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def get_solution_record(self):
                return self.solution_record

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def save_to_file(self, file_name):
                with open(file_name, "wb") as out_file:
                        csv_obj = csv.writer(out_file)
                        csv_obj.writerows(self.solution_record)

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def load_from_file(self, file_name):
                result = []
                with open(file_name, "rb") as in_file:
                        file_reader = csv.reader(in_file, delimiter=',')
                        for row in file_reader:
                                result.append(row)
                self.solution_record = result

