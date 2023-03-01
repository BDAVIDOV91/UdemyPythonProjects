import pandas as pd
from bokeh.plotting import figure, output_file, show
 
df=pd.read_excel("verlegenhuken.xlsx",sheet_name=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10
 
p=figure(width=500,height=400,tools='pan')

 
p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"    
 
p.circle(df["Temperature"],df["Pressure"],size=0.5)
output_file("WeatherGraphs.html")
show(p)
