

# Initial implementation of the Simulated Annealing Algorithm

import random as r
import math as m
#from ObjectiveFunction import MinimisingFunction as minfun
#from ObjectiveFunction import MaximisingFunction as maxfun


class Montecarlo():
        # def function(x):
        #   # x^3 - x^2 + 2x - 7
        #   return x ** 3 - x ** 2 + 2 * x - 7

        alpha = 0.95 #Value for cooling schedule

        def __init__(self, dataset, solution, mutator, obj_func, status):
                self.dataset = dataset
                self.solution = solution
                self.mutator = mutator
                self.obj_func = obj_func
                self.status = status

        def run(self, alpha, initial_c):
                iterations = 0
                max_iter = self.status.get_max_iterations()

                self.status.set_alpha_value_sa(alpha)

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

                        #print(y_temp)
                        #print(y)
                        #print("---")

                        #Calculate change of energy
                        energy_change = y_temp - y

                        #Determining if the random state should be
                                #accepted as the new state
                        if energy_change <= 0:
                                x = x_temp
                                y = y_temp
                        else:
                                #The new state is accepted if a random number is less than
                                        #the calculated probability
                                #print("The values for c and energy change")
                                #print(c)
                                #print(energy_change)
                                #print("----------")
                                if m.exp(energy_change / c) < r.random():
                                        x = x_temp
                                        y = y_temp

                        #print(c)

                        #Update status parameters



                        #Add entry to solution_record

                if y < 0:
                        y *= -1
                print("The Global Minimum value calculated after " + str(iterations) + " iterations is")
                print("x = " + str(x) + " and y = " + str(y))
                #print("From the dataset: ")
                #print(self.dataset)

                return self.status