from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Define the coordinates for the points
x = [3, 4, 5, 6, 7, 8, 9, 10]
y = [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

# Define the size and color of the triangles
triangle_size = 30
triangle_color = "blue"

# Create a ColumnDataSource object
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a figure with triangles as glyphs
p = figure(title="Graph with triangles as glyphs", x_axis_label="X-axis", y_axis_label="Y-axis")
p.triangle(x='x', y='y', size=triangle_size, color=triangle_color, source=source)

# Show the plot
show(p)
