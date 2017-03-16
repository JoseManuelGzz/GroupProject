"""
<class name>: <class description/objective>
        (?)<subclass name>: <subclass description/objective>
"""

import csv
class Status:

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


        def add_iteration(self):
                self.num_iter = self.num_iter + 1

        def add_function_calls(self):
                self.func_calls = self.func_calls + 1

        def add_function_evaluation(self, func_value):
                self.func_evaluation.append(func_value)

        def add_c_sa_parameters(self, c_value):
                self.sa_parameters["c"].append(c_value)

        def add_solution_record_entry(self, entry):
                self.solution_record.append(entry)

        def set_alpha_value_sa(self, alpha):
                self.sa_parameters['alpha'] = alpha

        def set_elapsed_time(self, elapsed_time):
                self.elapsed_time = elapsed_time

        def get_function_calls(self):
                return self.func_calls

        def get_max_iterations(self):
                return self.max_iter

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

