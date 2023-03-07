from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

# Debugging step: print the type of df
print(type(df))

# Convert datetime values to string values for display purposes
df['Start_string'] = df['Start'].dt.strftime('%d-%m-%Y %H:%M:%S')
df['End_string'] = df['End'].dt.strftime('%d-%m-%Y %H:%M:%S')

# Debugging step: print the DataFrame columns
print(df.columns)

# Create a ColumnDataSource object from the DataFrame for plotting purposes
cds = ColumnDataSource(df)


# Create a Bokeh figure object with specific properties
p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode = 'scale_width', title='Motion Graph')
p.yaxis.minor_tick_line_color = None

# Add a hover tool to display information about each bar on the graph
hover = HoverTool(tooltips=[('Start', '@Start_string'), ('End', '@End_string')])
p.add_tools(hover)

# Create a green bar for each time interval
q = p.quad(left='Start', right='End', bottom=0, top=1, color='green', source=cds)


# Specify the output file and show the graph
output_file('Graphs.html')
show(p)
