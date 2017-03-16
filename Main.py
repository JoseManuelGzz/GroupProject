from Dataset import Dataset
from ObjectiveFunction import CSPObjectiveFunction
from ObjectiveFunction import FFMSPObjectiveFunction
from Mutator import Mutator
from SAAlgorithm_Draft import SAAlgorithm
from Montecarlo import Montecarlo
from Status import Status
from Solution import Solution
from Figures import Figure

columns = 10 #300

rows = 7 #100

max_iterations = 5000 #5000

alphabet=range(0,5)

alpha = 0.95

initial_c = 200

status = Status(max_iterations, rows, columns, len(alphabet))

dataset = Dataset(rows= rows, cols = columns, alphabet=alphabet)


data = dataset.get_data()

mutator = Mutator(dataset)

solution = Solution(dataset)

solution_data = solution.get_solution('csp')


"""
print(solution_data)
x = mutator.use_random_flip_2(solution_data, 0.3)
print(x)
"""

min_obj_f = CSPObjectiveFunction()
max_obj_f = FFMSPObjectiveFunction(0.75 * columns)


#def _init_(self, dataset, solution, mutator, obj_func):


sa = Montecarlo(data, solution_data, mutator, min_obj_f, status)
"""
solution_data = solution.get_solution('ffmsp')

sa_ffmsp = SAAlgorithm(data, solution_data, mutator, max_obj_f, status)
"""
status = sa.run(alpha, initial_c)
status.save_to_file('csp_run.csv')
"""
status = sa_ffmsp.run_ffmsp(alpha, initial_c)
status.save_to_file('ffmsp_run.csv')

"""
#figure = Figure(status)
#figure.show_best_result_plot()
#figure.save_best_result_plot("best_result.png")
#figure.show_current_result_plot()
#figure.save_current_result_plot("current_result.png")





