# Making a basic Bokeh line graph.

# importing bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Prepare some data.
x = [1,2,3,4,5]
y = [6,7,8,9,10]


# Prepare the output file.
output_file('line.html')


# Create a figure object.
f = figure()


# Create line plot.
f.line(x,y)


# Write the plot in the figure object.
show(f)
