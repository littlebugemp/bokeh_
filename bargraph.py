# importing the modules
from bokeh.plotting import figure, output_file, show

# file to save the model
output_file("gfg.html")
	
# instantiating the figure object
graph = figure(title = "Bokeh Vertical Bar Graph")

# x-coordinates to be plotted
x = [1, 2, 3, 4, 5]

# x-coordinates of the top edges
top = [1, 2, 3, 4, 5]

# width / thickness of the bars
width = 0.5

# plotting the graph
graph.vbar(x,
		top = top,
		width = width)

# displaying the model
show(graph)
