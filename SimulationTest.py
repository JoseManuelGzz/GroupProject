from Simulation import SimulationSA_CSP
from Simulation import SimulationSA_FFMSP
from Simulation import SimulationMCM_CSP
from Simulation import SimulationMCM_FFMSP
from Simulation import SimulationEv_CSP
from Simulation import SimulationEv_FFMSP
from Simulation import SimulationGA_CSP
from Simulation import SimulationGA_FFMSP
from Figures import Figure

# sa_csp = SimulationSA_CSP(10,7,5000,range(0,5),0.75,'RandomFlip', 0.95,200)
# sa_csp.get_solution()
# sa_csp_figure = Figure(sa_csp.status)
# sa_csp_fig1 = sa_csp_figure.get_best_result_plot_html()
# sa_csp_fig2 = sa_csp_figure.get_current_result_plot_bokeh()
# sa_csp_figure.save_multiple_plots_bokeh("sa_csp.html",[sa_csp_fig1,sa_csp_fig2])

# sa_ffmsp = SimulationSA_FFMSP(10,7,5000,range(0,5),0.75,'RandomFlip', 0.95,200)
# sa_ffmsp.get_solution()
# sa_ffmsp_figure = Figure(sa_ffmsp.status)
# sa_ffmsp_fig1 = sa_csp_figure.get_best_result_plot_html()
# sa_ffmsp_fig2 = sa_csp_figure.get_current_result_plot_bokeh()
# sa_ffmsp_figure.save_multiple_plots_bokeh("sa_ffmsp.html",[sa_ffmsp_fig1,sa_ffmsp_fig2])

# mcm_csp = SimulationMCM_CSP(10,7,5000,range(0,5),0.75,'RandomFlip',200)
# mcm_csp.get_solution()
# mcm_csp_figure = Figure(mcm_csp.status)
# mcm_csp_fig1 = mcm_csp_figure.get_best_result_plot_html()
# mcm_csp_fig2 = mcm_csp_figure.get_current_result_plot_bokeh()
# mcm_csp_figure.save_multiple_plots_bokeh("mcm_csp.html",[mcm_csp_fig1,mcm_csp_fig2])

# mcm_ffmsp = SimulationMCM_FFMSP(10,7,5000,range(0,5),0.75,'RandomFlip',200)
# mcm_ffmsp.get_solution()
# mcm_ffmsp_figure = Figure(mcm_ffmsp.status)
# mcm_ffmsp_fig1 = mcm_ffmsp_figure.get_best_result_plot_html()
# mcm_ffmsp_fig2 = mcm_ffmsp_figure.get_current_result_plot_bokeh()
# mcm_ffmsp_figure.save_multiple_plots_bokeh("mcm_ffmsp.html",[mcm_ffmsp_fig1,mcm_ffmsp_fig2])

# ev_csp = SimulationEv_CSP(10,7,5000,range(0,5),0.75,'RandomFlip',10)
# ev_csp.get_solution()
# ev_csp_figure = Figure(ev_csp.status)
# ev_csp_fig1 = ev_csp_figure.get_best_result_plot_html()
# ev_csp_fig2 = ev_csp_figure.get_current_result_plot_bokeh()
# ev_csp_figure.save_multiple_plots_bokeh("ev_csp.html",[ev_csp_fig1,ev_csp_fig2])

# ev_ffmsp = SimulationEv_FFMSP(10,7,5000,range(0,5),0.75,'RandomFlip',10)
# ev_ffmsp.get_solution()
# ev_ffmsp_figure = Figure(ev_ffmsp.status)
# ev_ffmsp_fig1 = ev_ffmsp_figure.get_best_result_plot_html()
# ev_ffmsp_fig2 = ev_ffmsp_figure.get_current_result_plot_bokeh()
# ev_ffmsp_figure.save_multiple_plots_bokeh("ev_ffmsp.html",[ev_ffmsp_fig1,ev_ffmsp_fig2])

ga_csp = SimulationGA_CSP(10,7,5000,range(0,5,),0.75,'RandomFlip')
ga_csp.get_solution()
ga_csp_figure = Figure(ga_csp.status)
ga_csp_fig1 = ga_csp_figure.get_best_result_plot_html()
ga_csp_fig2 = ga_csp_figure.get_current_result_plot_bokeh()
ga_csp_figure.save_multiple_plots_bokeh("ga_csp.html",[ga_csp_fig1,ga_csp_fig2])

ga_ffmsp = SimulationGA_FFMSP(10,7,5000,range(0,5),0.75,'RandomFlip')
ga_ffmsp.get_solution()
# ga_ffmsp_figure = Figure(ga_ffmsp.status)
# ga_ffmsp_fig1 = ga_ffmsp_figure.get_best_result_plot_html()
# ga_ffmsp_fig2 = ga_ffmsp_figure.get_current_result_plot_bokeh()
# ga_ffmsp_figure.save_multiple_plots_bokeh("ga_ffmsp.html",[ga_ffmsp_fig1,ga_ffmsp_fig2])



