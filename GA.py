from Mutator import Mutator
#import matplotlib.pyplot as plt  
import math 
import random

class GA:
    # create the input string

    def __init__(self, dataset, solution, mutator, obj_func, rows, chrom_length):
        self.dataset = dataset
        self.results = [[]]  
        self.solution = solution
        self.mutator = mutator
        self.obj_func = obj_func
        self.rows = rows
        self.chrom_length = chrom_length

    #def print_min_fun(a, b):
#        return len(filter(lambda x: x >= t, distances))


        
      
    # compute the fit value by objective object
      
    def calobjValue(self):  
        temp1 = self.solution
        data = self.dataset
        obj_value = []
        chrom_length = 10  
        for i in range(len(temp1)):  
            obj_value_ = 11 - self.obj_func.evaluate(data,temp1[i])
            obj_value.append(obj_value_)
        return obj_value
     
    # choose the value more than min
      
    def calfitValue(self, obj_value):  
        fit_value = []  
        c_min = 0  
        for i in range(len(obj_value)):  
            if(obj_value[i] > _min):  
                temp = obj_value[i]  
            else:  
                temp = 0.0  
            fit_value.append(temp)  
        return fit_value



      
    import random  
      
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


    def mutation(self, pm):  
        px = len(self.solution)  
        py = len(self.solution[0])  
          
        for i in range(px):  
            if(random.random() < pm):  
                mpoint = random.randint(0, py-1)
                self.solution[i][mpoint] == random.randint(0,4)
                #if(self.solution[i][mpoint] == 1):  
                    #self.solution[i][mpoint] = 0  
                #else:  
                    #self.solution[i][mpoint] = 1


    # select the string which probobility left is high
      
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


    def best(self, fit_value):
        return self.solution[fit_value.index(max(fit_value))], max(fit_value)
        





    def run(self):
        
        solution_size = self.rows
        chrom_length = self.chrom_length     
        pc = 0.3           
        pm = 0.01            
        dataset = self.dataset
        fit_value = []       
        fit_mean = []
        solution = self.solution
         
             
        for i in range(solution_size):  
            fit_value = self.calobjValue()             
            best_individual, best_fit = self.best(fit_value)
            self.results.append([11-best_fit, best_individual]) 
            self.selection(fit_value)      
            self.crossover(pc)     
            self.mutation(pm)

        self.results = self.results[1:]  
        self.results.sort()  
          
  
        #print self.results
        print self.results[0]
        


