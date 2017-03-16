import math 
import random

class GA:
    # create the input string

    def __init__(self, dataset, solution, mutator, obj_func, status):
        self.dataset = dataset
        self.results = [[]]  
        self.solution = solution
        self.mutator = mutator
        self.obj_func = obj_func
        self.status = status


        
      
    # compute the fit value by objective object
      
    def csp_fit_value(self):  
        temp1 = self.solution
        data = self.dataset
        fit_value = []
        for i in range(len(temp1)):  
            fit_value_ = 11 - self.obj_func.evaluate(data,temp1[i])
            fit_value.append(fit_value_)
        return fit_value



    def ffmsp_fit_value(self):  
        temp1 = self.solution
        data = self.dataset
        fit_value = []
        for i in range(len(temp1)):
            fit_value_ = self.obj_func.evaluate(data,temp1[i])
            fit_value.append(fit_value_)
        return fit_value
    

      
    # compute the sum of fit_value

    def sum(self,fit_value):  
        total = 0  
        for i in range(len(fit_value)):  
            total += fit_value[i]  
        return total  


      
    # compute the probability of fit_value
     
    def cumsum(self,fit_value):  
        for i in range(len(fit_value)-2, -1, -1):  
            t = 0  
            j = 0  
            while(j <= i):  
                t += fit_value[j]  
                j += 1  
            fit_value[i] = t  
            fit_value[len(fit_value)-1] = 1



    # mutate the solutions
    def mutation(self, probability_of_mutation):  
        solution_length = len(self.solution)  
        for i in range(solution_length): 
	    self.mutator.use_random_flip_2(self.solution[i], probability_of_mutation)  
		
                

    # select the string which probibility left is high
      
    def selection(self, fit_value):  
        newfit_value = []  
       
        total_fit = sum(fit_value)  
        for i in range(len(fit_value)):  
            newfit_value.append(fit_value[i] / total_fit)  

        self.cumsum(newfit_value)  
        ms = []  
        solution_len = len(self.solution)  
        for i in range(solution_len):  
            ms.append(random.random())  
        ms.sort()  
        fitin = 0  
        newin = 0  
        newsolution = self.solution
        
        while newin < solution_len:  
            if(ms[newin] < newfit_value[fitin]):  
                newsolution[newin] = self.solution[fitin]  
                newin = newin + 1  
            else:  
                fitin = fitin + 1  
        self.solution = newsolution



    # compulate
      
    def crossover(self, pc):  
        solution_len = len(self.solution)  
        for i in range(solution_len - 1):  
            if(random.random() < pc):  
                cpoint = random.randint(0,len(self.solution[0]))  
                temp1 = []  
                temp2 = []  
                temp1.extend(self.solution[i][0:cpoint])  
                temp1.extend(self.solution[i+1][cpoint:len(self.solution[i])])  
                temp2.extend(self.solution[i+1][0:cpoint])  
                temp2.extend(self.solution[i][cpoint:len(self.solution[i])])  
                self.solution[i] = temp1  
                self.solution[i+1] = temp2

    # find the best sequence of solutions

    def best(self, fit_value):
        return self.solution[fit_value.index(max(fit_value))], max(fit_value)
        

    # objective problem is CSP

    def run(self, iterations, probability_of_mutation = 0.1):    
        #probability_of_crossover = 0.3           
        #probability_of_mutation = 0.01            
        fit_value = []
        self.status.add_function_calls()
	self.status.set_iterations_value_ga(iterations)
	self.status.set_probability_of_mutation_ga(probability_of_mutation)
	###################
	print("------------1----")
	print("Dataset: ")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.dataset]))
	#print(self.dataset)
             
	
	
	###################
	print("------------2----")
	print("Initial Solutions")
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.solution]))

	###################
	print("------------3----")
	fit_value0 = self.csp_fit_value()
	best_individual, best_fit = self.best(fit_value0)
	print("Best initial solution: ")
	print(best_individual)
	print("Evaluation of best solution: ")
	print(11 - best_fit)

	###################
	print("------------4----")
        print("Iterations: ")
	print(iterations)



	###################
        for i in range(iterations):  
            fit_value = self.csp_fit_value()             
            best_individual, best_fit = self.best(fit_value)
            self.results.append([11-best_fit, best_individual]) 
            self.selection(fit_value)      
            #self.crossover(probability_of_crossover)     
            self.mutation(probability_of_mutation)
        
	###################
  	self.results = self.results[1:]  
        self.results.sort()
        self.status.add_solution_record_entry(self.results)
        #print self.results
	print("Result: ")
	print("   Solution: ")
	print self.results[0][1]
	print("   Evaluation: ")
	print(self.results[0][0])
        #print self.results[0]
	return self.status



    # objective problem is FFMSP

    def run_ffmsp(self, iterations, probability_of_mutation = 0.1):     
        #probability_of_crossover = 0.3           
        #probability_of_mutation = 0.01            
        fit_value = []       
	self.status.add_function_calls()
	self.status.set_iterations_value_ga(iterations)
	self.status.set_probability_of_mutation_ga(probability_of_mutation)
	###################
	print("------------1----")
	print("Dataset: ")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.dataset]))
             
	
	
	###################
	print("------------2----")
	print("Initial Solutions")
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.dataset]))

	###################
	print("------------3----")
	fit_value = self.ffmsp_fit_value()
	best_individual, best_fit = self.best(fit_value)
	print("Best initial solution: ")
	print(best_individual)
	print("Evaluation of best solution: ")
	print(best_fit)

	###################
	print("------------4----")
        print("Iterations: ")
	print(iterations)



	###################
        for i in range(iterations):  
            fit_value = self.ffmsp_fit_value()             
            best_individual, best_fit = self.best(fit_value)
            #self.results.append([best_fit, best_individual]) 
            self.selection(fit_value)      
            #self.crossover(probability_of_crossover)     
            self.mutation(probability_of_mutation)
        
	###################
  	self.results = self.results[1:]  
        self.results.sort()
        self.status.add_solution_record_entry(self.results)
        #print self.results
	print("Result: ")
	print("   Solution: ")
	print(self.results[0][1])
	print("   Evaluation: ")
	print(self.results[0][0])
        #print self.results[0]
	return self.status
