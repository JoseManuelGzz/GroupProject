

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

        def print_min_fun(a, b):
                y_min = 100000
                y_temp = 0
                x_min = 0
                while a <= b:
                        y_temp = function(a)
                        if y_temp < y_min:
                                y_min = y_temp
                                x_min = a
                        a = a + 1
                print("The minimum value is y =" + str(y_min) + " in x = " + str(x_min))

        # number: the number of random numbers to be discarded
        # seed: the seed for the random number generator
        def prepare_random_numbers(number, seed):
                r.seed(seed)
                for i in range(number):
                        r.random()
                print(r.random())

        # function that creates a list of distances from each sequence to a given string
        def calculate_hamming_distances(sequences, string):
                result = []
                dist = 0
                for sequence in sequences:
                        #Add 1 if elements are different, 0 if they are the same
                        for i in range(len(sequence)):
                                if sequence[i] != string[i]:
                                        dist = dist + 1
                        result.append(dist)
                        dist = 0
                return result

        def csp_cost_function(distances):
                return max(distances)

        def ffmsp_cost_function(distances, t):
                return len(filter(lambda x: x >= t, distances))

        def cooling_value(self, alpha, current_c, max_iterat, curr_iter):
                return alpha * current_c#((max_iterat - curr_iter)/(max_iterat * 1.0)) * current_c


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
                        x_temp = self.mutator.use_random_flip_2(self.solution, 0.3)

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

        def run_ffmsp(self, alpha, initial_c):
                iterations = 0
                max_iter = self.status.get_max_iterations()
                ###################
                print("------------1----")
                print("Dataset")
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.dataset]))
                print("-------")

                ###################
                self.status.set_alpha_value_sa(alpha)

                #Add mutator operator
                x = self.solution
                y = self.obj_func.evaluate(self.dataset, x)
                self.status.add_function_calls()

                ######
                print("------------2----")
                print("Initial Solution")
                solution_print = "    "
                for ch in x:
                        solution_print = solution_print + str(ch)
                        solution_print = solution_print + "  "
                print(solution_print)
                print("------------3----")
                print("Initial solution evaluation")
                print(y)
                ######

                c = float(initial_c) # Control parameter, defined by the function of Temperature

                #####
                print("------------4----")
                print("Initial c")
                print(c)
                #####
                
                x_temp = 0
                y_temp = 0

                energy_change = 0

                while iterations <= max_iter: #and c >= 0.005:
                        
                        self.status.add_c_sa_parameters(c)

                        #Get random new state
                        x_temp = self.mutator.use_random_flip_2(self.solution, 0.3)

                        y_temp = self.obj_func.evaluate(self.dataset, x_temp)
                        self.status.add_function_calls()

                        #####
                        
                        if iterations < 3:
                                print("------------5----")
                                print("Mutated Solution:")
                                print(x_temp)
                                print("Evaluated solution:")
                                print(y_temp)
                        #####

                        iterations = iterations + 1
                        self.status.add_iteration()

                        current_entry = [iterations, self.status.get_function_calls(), y, y_temp]
                        self.status.add_solution_record_entry(current_entry)

                        #print(y_temp)
                        #print(y)
                        #print("---")

                        #Calculate change of energy
                        energy_change = y - y_temp
                        #####
                        if iterations < 3:
                                print("------------6----")
                                print("f(current_sol) - f(new_sol):")
                                print(energy_change)
                        #####

                        #Determining if the random state should be
                                #accepted as the new state
                        if energy_change <= 0:
                                x = x_temp
                                y = y_temp
                                #####
                                if iterations < 3:
                                        print("------------7----")
                                        print("Improvement! Changing current sol.")
                                #####
                        else:
                                #The new state is accepted if a random number is less than
                                        #the calculated probability
                                
                                #####
                                if iterations < 3:
                                        print("------------8----")
                                        print("No improvement, updating if exp(energy_change/c) > random()")
                                #####

                                # print("Energy Change " + str(energy_change))
                                # print("C value " + str(c))
                                # print("Division " + str(energy_change / (c*1.0)))
                                if m.exp(energy_change / (c)) < r.random():
                                        #####
                                        if iterations < 3:
                                                print("------------9----")
                                                print("Updating sol. even without improv.")
                                        #####
                                        x = x_temp
                                        y = y_temp



                        if c >= 0.05:
                                #####
                                if iterations < 3:
                                        print("------------10----")
                                        print("Updating c value with " + str(self.alpha) + "*current_c")
                                #####
                                c = self.cooling_value(alpha, c, max_iter, iterations)
                        #print(c)

                        #Update status parameters



                        #Add entry to solution_record


                print("The Global Minimum value calculated after " + str(iterations) + " iterations is")
                print("x = " + str(x) + " and y = " + str(y))
                #print("From the dataset: ")
                #print(self.dataset)

                return self.status

