from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Define the coordinates for the points
x = [3, 4, 5, 6, 7, 8, 9, 10]
y = [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

# Define the size and color of the circles
circle_size = 30
circle_color = "red"

# Create a ColumnDataSource object
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a figure with circles as glyphs
p = figure(title="Graph with circles as glyphs", x_axis_label="X-axis", y_axis_label="Y-axis")
p.circle(x='x', y='y', size=circle_size, color=circle_color, source=source)

# Show the plot
show(p)
