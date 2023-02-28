import pandas as pd
from bokeh.plotting import figure, output_file, show

# Reading the Excel file using pandas.
df = pd.read_excel('verlegenhuken.xlsx')

# Convert temperature and pressure values.
df['Temperature'] = df['Temperature'] / 10.0
df['Pressure'] = df['Pressure'] / 10.0

# Set up Bokeh figure.
p = figure(title= 'Temperature vs Pressure', x_axis_label = 'Temperature(Celsius)', y_axis_label= 'Pressure (kPa)')

#Add scatter plot data.

p.scatter(df['Temperature'], df['Pressure'], color = 'blue')

# Set font and color properties.
p.title.text_font_size = '20pt'
p.title.text_font = 'Arial'
p.xaxis.axis_label_text_font_size = '16pt'
p.xaxis.axis_label_text_font = 'Helvetica'
p.yaxis.axis_label_text_font_size = '16pt'
p.yaxis.axis_label_text_font = 'Helvetica'
p.xaxis.major_label_text_font_size = '12pt'
p.yaxis.major_label_text_font_size = '12pt'
p.xaxis.major_label_text_font = 'Verdana'
p.yaxis.major_label_text_font = 'Verdana'

# Save and show the plot.
output_file('Weather Graphs.html')
show(p)