import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import DataFrame as df

class Figure:
    def __init__(self, status):
        self.status = status
        self.record = df(status.get_solution_record(), columns=['iteration', 'num_func_calls', 'current_best', 'current_soln'] )

    def get_best_result_plot(self,marker="_", marker_size=2):
        sns_plot = sns.lmplot(self.record.columns[0], self.record.columns[2], data=pd.concat([self.record['iteration'], self.record['current_best']], axis=1),
                              scatter_kws={"s": marker_size}, fit_reg=False, markers=marker)
        #sns_plot = sns.pairplot(data=self.record)
        sns_plot.axes[0, 0].set_ylim(0, )
        sns_plot.axes[0, 0].set_xlim(0, )
        sns.plt.show()
        plt.clf()
        #return sns_plot


    def save_best_result_plot(self, file_name, marker="_", marker_size=2):
        sns_plot = sns.lmplot(self.record.columns[0], self.record.columns[2], data=pd.concat([self.record['iteration'], self.record['current_best']], axis=1),
                              scatter_kws={"s": marker_size},fit_reg=False, markers=marker )
        #sns_plot = sns.pairplot(data=self.record)
        sns_plot.axes[0, 0].set_ylim(0, )
        sns_plot.axes[0, 0].set_xlim(0, )
        sns_plot.savefig(file_name)
        plt.clf()
        #sns.plt.show()
        #return sns_plot

    def get_current_result_plot(self,marker="_", marker_size=2):
        sns_plot = sns.lmplot(self.record.columns[0], self.record.columns[3], data=pd.concat([self.record['iteration'], self.record['current_soln']], axis=1),
                              scatter_kws={"s": marker_size}, fit_reg=False, markers=marker)
        #sns_plot = sns.pairplot(data=self.record)
        sns_plot.axes[0, 0].set_ylim(0, )
        sns_plot.axes[0, 0].set_xlim(0, )
        sns.plt.show()
        plt.clf()
        #return sns_plot