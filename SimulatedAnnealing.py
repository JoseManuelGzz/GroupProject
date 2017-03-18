import random as r
import math as m

"""
SAAlgorithm: Class that implements the Simulated Annealing optimization
                Algorithm for String Consensus problems
"""
class SAAlgorithm():

        '''
        <__init__>
                Constructor for the class
                parameters:
                        <self> - Pointer to the current object
                        <dataset> - List of lists containing 
                                same length sequences of characters
                        <solution> - list of characters with the same
                                length of the sublists in the dataset
                                parameter
                        <mutator> - Mutator object that generates new 
                                solution sequences based on a given
                                sequence
                        <obj_func> - ObjectiveFunction object that produces 
                                a numeric evaluation of a sequence and a 
                                dataset (based on Hamming distances)
                        <status> - Status object that contains a record of 
                                each run of an algorithm
                returns:
                        -None-

        '''
        def __init__(self, dataset, solution, mutator, obj_func, status):
                self.dataset = dataset
                self.solution = solution
                self.mutator = mutator
                self.obj_func = obj_func
                self.status = status

        '''
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        '''
        def cooling_value(self, alpha, current_c, max_iterat, curr_iter):
                return alpha * current_c#((max_iterat - curr_iter)/(max_iterat * 1.0)) * current_c

        """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

        """
        def run(self, alpha, initial_c):
                iterations = 0
                max_iter = self.status.get_max_iterations()

                self.status.set_alpha_value_sa(alpha)

                #Add mutator operator
                x = self.solution
                y = self.obj_func.evaluate(self.dataset, x)
                self.status.add_function_calls()

                # Control parameter, defined by the function of Temperature
                c = initial_c 

                x_temp = 0
                y_temp = 0

                energy_change = 0

                while iterations <= max_iter: # and c > 0.0:
                        
                        self.status.add_c_sa_parameters(c)

                        #Get random new state
                        x_temp = self.mutator.mutate(self.solution)

                        #Evaluate random new state
                        y_temp = self.obj_func.evaluate(self.dataset, x_temp)
                        
                        self.status.add_function_calls()

                        iterations = iterations + 1
                        self.status.add_iteration()

                        current_entry = [iterations, self.status.get_function_calls(), y, y_temp]
                        self.status.add_solution_record_entry(current_entry)

                        #Calculate change of energy
                        energy_change = y_temp - y

                        #Determining if the random state should be accepted as the new state
                        if energy_change <= 0:
                                x = x_temp
                                y = y_temp
                        else:
                                #The new state is accepted if a random number is less than the calculated probability
                                if m.exp(energy_change / c) < r.random():
                                        x = x_temp
                                        y = y_temp



                        if c > 0.1:
                                c = self.cooling_value(alpha, c, max_iter, iterations)

                #Change the sign for the FFMSP solution
                if y < 0:
                        y *= -1

                #Print the results
                print("The Global Minimum value calculated after " + str(iterations) + " iterations is")
                print("x = " + str(x) + " and y = " + str(y))

                return self.status

