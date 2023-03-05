from bokeh.plotting import figure, output_file, show
import pandas as pd

# Read the data from the URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
df = pd.read_csv(url, parse_dates=["year"])

# Create the Bokeh figure
p = figure(width=800, height=400, x_axis_type="datetime")

# Add the line plot
p.line(df["year"], df["passengers"], line_color="blue", line_width=2)

# Set the output file and show the plot
output_file("flights.html")
show(p)


