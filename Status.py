
class Status:


        """def __init__(self):
                num_sequences = 0
                sequence_length = 0
                alphabet_size = 0
                num_iter = 0
                max_iter = 0
                func_calls = 0
                func_evaluation = []
                elapsed_time = 0.0
                sa_parameters = {'c': [], 'alpha': 0}
                ga_parameters = {}
                mcm_parameters = {}
                re_parameters = {}
                solution_record = []"""

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

        def add_add_solution_record_entry(self, entry):
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
