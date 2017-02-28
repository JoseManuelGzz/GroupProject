# create the input string

def geneEncoding(pop_size, chrom_length):  
    pop = [[]]  
    for i in range(pop_size):  
        temp = []  
        for j in range(chrom_length):  
            temp.append(random.randint(0, 1))  
        pop.append(temp)  
  
    return pop[1:]


  
import math  
  
# compute the fit value by objective object
  
def calobjValue(pop, dataset):  
    temp1 = pop 
    obj_value = []
    chrom_length = len(x)  
    for i in range(len(temp1)):  
        obj_value = objective_promblem(pop, dataset) 
    return obj_value
 
# choose the value more than min
  
def calfitValue(obj_value):  
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

def sum(fit_value):  
    total = 0  
    for i in range(len(fit_value)):  
        total += fit_value[i]  
    return total  
  
# compute the probability of fit_value
 
def cumsum(fit_value):  
    for i in range(len(fit_value)-2, -1, -1):  
        t = 0  
        j = 0  
        while(j <= i):  
            t += fit_value[j]  
            j += 1  
        fit_value[i] = t  
        fit_value[len(fit_value)-1] = 1  

# select the string which probobility left is high
  
def selection(pop, fit_value):  
    newfit_value = []  
   
    total_fit = sum(fit_value)  
    for i in range(len(fit_value)):  
        newfit_value.append(fit_value[i] / total_fit)  

    cumsum(newfit_value)  
    ms = []  
    pop_len = len(pop)  
    for i in range(pop_len):  
        ms.append(random.random())  
    ms.sort()  
    fitin = 0  
    newin = 0  
    newpop = pop  
    
    while newin < pop_len:  
        if(ms[newin] < newfit_value[fitin]):  
            newpop[newin] = pop[fitin]  
            newin = newin + 1  
        else:  
            fitin = fitin + 1  
    pop = newpop



import random  

# compulate
  
def crossover(pop, pc):  
    pop_len = len(pop)  
    for i in range(pop_len - 1):  
        if(random.random() < pc):  
            cpoint = random.randint(0,len(pop[0]))  
            temp1 = []  
            temp2 = []  
            temp1.extend(pop[i][0:cpoint])  
            temp1.extend(pop[i+1][cpoint:len(pop[i])])  
            temp2.extend(pop[i+1][0:cpoint])  
            temp2.extend(pop[i][cpoint:len(pop[i])])  
            pop[i] = temp1  
            pop[i+1] = temp2







import mutation
  
pop_size = 500 
chrom_length = 10      
pc = 0.6           
pm = 0.01            
results = [[]]       
fit_value = []       
fit_mean = []       
 
pop = geneEncoding(pop_size, chrom_length)  
  
for i in range(pop_size):  
    obj_value = calobjValue(pop, chrom_length, max_value) 
    fit_value = calfitValue(obj_value) 
    selection(pop, fit_value)      
    crossover(pop, pc)     
    mutation(pop, pm)       
  
  

