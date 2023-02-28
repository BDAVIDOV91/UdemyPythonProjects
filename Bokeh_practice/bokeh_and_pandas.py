# Making a bokeh basic line graph.

# Importing bokeh and Pandas.
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# Prepare some data.
df = pandas.read_csv('bachelors.csv')
x = df['Year']
y = df['Engineering']

# Preparing the output file.
output_file('Education Data.html')

# Create a figure object.
f = figure()

# Create line plot.
f.line(x,y)

# Write the plot in the figure object.
show(f)