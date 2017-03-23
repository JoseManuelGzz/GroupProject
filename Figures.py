"""
Figures: <Description>
"""

import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as mpb
import seaborn as sns
import pandas as pd
from pandas import DataFrame as df
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot


class Figure:
    """
        __init__
                COnstructor for the Figures class
                parameters:
                        status - An instance of Status class used to get the plotting data from
                returns:
                        -None-

    """
    def __init__(self, status):
        self.status = status
        self.record = df(status.get_solution_record(), columns=['iteration', 'num_func_calls', 'current_best', 'current_soln'] )

    """
        show_best_result_plot
                Draws a trace plot for best result on the y_axis and iterations on the x-axis
                parameters:
                        marker_size (optional) - To control the size of the trace marker
                returns:
                        -None-

    """
    def show_best_result_plot(self,marker="_", marker_size=2):
        #f = plt.figure(1)
        sns_plot = sns.lmplot(self.record.columns[0], self.record.columns[2], data=pd.concat([self.record['iteration'], self.record['current_best']], axis=1),
                              scatter_kws={"s": marker_size}, fit_reg=False, markers=marker)
        #sns_plot = sns.pairplot(data=self.record)
        sns_plot.axes[0, 0].set_ylim(0, )
        sns_plot.axes[0, 0].set_xlim(0, )
        #f.show()
        sns.plt.show()
        #plt.clf()

        #return sns_plot


    """
        save_best_result_plot
                Saves a trace plot for best result on the y_axis and iterations on the x-axis in the given filename
                parameters:
                        file_name (optional) - File name where the chart should be saved, if none provided then chart saved in a file "best_result.png"
                        marker_size (optional) - To control the size of the trace marker
                returns:
                        -None-

    """
    def save_best_result_plot(self, file_name="best_result.png", marker="_", marker_size=2):
        sns_plot = sns.lmplot(self.record.columns[0], self.record.columns[2], data=pd.concat([self.record['iteration'], self.record['current_best']], axis=1),
                              scatter_kws={"s": marker_size},fit_reg=False, markers=marker )
        #sns_plot = sns.pairplot(data=self.record)
        sns_plot.axes[0, 0].set_ylim(0, )
        sns_plot.axes[0, 0].set_xlim(0, )
        sns_plot.savefig(file_name)
        sns.plt.clf()
        #sns.plt.show()
        #return sns_plot

    """
        show_current_result_plot
                Draws a trace plot for current_result on the y_axis and iterations on the x-axis
                parameters:
                        marker_size (optional) - To control the size of the trace marker
                returns:
                        -None-

    """
    def show_current_result_plot(self):
        #sns_plot = sns.lmplot(self.record.columns[0], self.record.columns[3], data=pd.concat([self.record['iteration'], self.record['current_soln']], axis=1),     scatter_kws={"s": marker_size}, fit_reg=False, markers=marker)
        sns.set_style("darkgrid")
        plt.plot(self.record['iteration'], self.record['current_soln'])
        plt.axis([0,self.status.get_max_iterations(),0,self.status.sequence_length])
        plt.xlabel(self.record.columns[0])
        plt.ylabel(self.record.columns[3])
        plt.show()

    """
        save_current_result_plot
                Saves a trace plot for current_result on the y_axis and iterations on the x-axis in the given filename
                parameters:
                        file_name (optional) - File name where the chart should be saved, if none provided then chart saved in a file "current_result.png"
                        marker_size (optional) - To control the size of the trace marker
                returns:
                        -None-

    """
    def save_current_result_plot(self,file_name="current_result.png"):
        #sns_plot = sns.lmplot(self.record.columns[0], self.record.columns[3], data=pd.concat([self.record['iteration'], self.record['current_soln']], axis=1),     scatter_kws={"s": marker_size}, fit_reg=False, markers=marker)
        sns.set_style("darkgrid")
        plt.plot(self.record['iteration'], self.record['current_soln'])
        plt.axis([0,self.status.get_max_iterations(),0,self.status.sequence_length])
        plt.xlabel(self.record.columns[0])
        plt.ylabel(self.record.columns[3])
        plt.savefig(file_name)
        #plt.show()

    """
        save_multiple_plots
                Saves multiple plots the given filename (has to be a pdf type)
                parameters:
                        file_name  - PDF file name where the chart should be saved
                        figures - An iterator containing objects of the type Figure
                returns:
                        -None-

    """
    def save_multiple_plots(self, filename_pdf, figures):
        pdf = mpb.PdfPages(filename_pdf)
        for figure in figures:
            pdf.savefig(figure)
        pdf.close()

    """
                get_best_result_plot_html
                        Private function for getting a bokeh figure object for best_solution
                        parameters:
                                marker_size: Parameter for the line width of the chart, default value: 2
                        returns:
                                An instance of figure from the Bokeh library

            """

    def get_best_result_plot_html(self, marker_size=2, opt_title=''):
        p = figure(title="Best_result"+opt_title, x_axis_label=self.record.columns[0], y_axis_label=self.record.columns[2])
        p.line(self.record['iteration'], self.record['current_best'], legend=self.record.columns[2], line_width=marker_size)

        return p

    """
                    get_current_result_plot_html
                            Private function for getting a bokeh figure object for current_solution
                            parameters:
                                    marker_size: Parameter for the line width of the chart, default value: 2
                            returns:
                                    An instance of figure from the Bokeh library

                """

    def get_current_result_plot_bokeh(self, marker_size=2):
        p = figure(title="Current_result", x_axis_label=self.record.columns[0], y_axis_label=self.record.columns[3])
        p.line(self.record['iteration'], self.record['current_soln'], legend=self.record.columns[3], line_width=marker_size)
        return p

    """
                    save_multiple_plots_bokeh
                            Function for saving multiple charts in a grid layout using the Bokeh library
                            parameters:
                                    filename_html: The name of the html file where results should be saved
                                    figures: A list of figures of the type Bokeh.figure

                            Side effect:
                                    Displays the charts and saves them in the given file name. File overwritten if already present.
                            returns:
                                    -None-

                """

    def save_multiple_plots_bokeh(self, filename_html, figures):
        # pdf = matplotlib.backends.backend_pdf.PdfPages(filename_pdf)
        output_file(filename_html)
        p = gridplot(figures, toolbar_location=None, ncols=2, plot_width=250, plot_height=250)
        show(p)