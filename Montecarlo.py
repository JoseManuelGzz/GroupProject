import random as r
import math as m
import time

"""

Montecarlo: Class that implements the Montecarlo Metropolis optimization
                Algorithm for String Consensus problems

"""
class Montecarlo():
        """
        __init__
                Constructor of the Montecarlo class
                parameters:
                        self - Pointer to the object
                        dataset - A copy of the dataset object already initialised
                        solution - A copy of the solution object already initialised
                        mutator - A copy of the mutator object to be used
                        obj_func - A copy of the objective function object to be used
                        status - A copy of the status object where the results will be stored
                returns:
                        -None-
        """
        def __init__(self, dataset, solution, mutator, obj_func, status):
                self.dataset = dataset
                self.solution = solution
                self.mutator = mutator
                self.obj_func = obj_func
                self.status = status
        """
        run
                Method that gets the solution for the string consensus problem
                with all the parameters used to create the object, and prints 
                the results
                parameters:
                        self - Pointer to the object
                        initial_c - Initial value of the temperature
                returns:
                        -None-
        """
        def run(self, initial_c):
                start = time.time()
                iterations = 0
                max_iter = self.status.get_max_iterations()


                #Add mutator operator
                x = self.solution
                y = self.obj_func.evaluate(self.dataset, x)
                self.status.add_function_calls()

                c = initial_c # Control parameter, defined by the function of Temperature

                x_temp = 0
                y_temp = 0

                energy_change = 0

                while iterations <= max_iter: #and c >= 0.005:
                        
                        self.status.add_c_sa_parameters(c)

                        #Get random new state
                        x_temp = self.mutator.mutate(self.solution)

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

                end = time.time()
                # Print the results
                print("The Global Minimum value calculated after " + str(iterations) + " iterations is")
                print("x = " + str(x) + " and y = " + str(y))

                # Store the best solution in the corresponding status attribute
                self.status.set_best_solution(x)
                self.status.set_elapsed_time(end-start)

                return self.status