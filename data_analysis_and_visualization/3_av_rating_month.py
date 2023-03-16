import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

# Read data from CSV file and parse the 'Timestamp' column as datetime
data = pandas.read_csv('reviews.csv', parse_dates = ['Timestamp'])
# Add a new column 'Month' to group reviews by month
data['Month'] = data['Timestamp'].dt.strftime('%Y %m')
# Calculate the average rating per month using groupby()
month_average = data.groupby(['Month']).mean()

# Define the chart options in a JSON string
chart_def = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude',
    align: 'left'
  },
  subtitle: {
    text: 'According to the Standard Atmosphere Model',
    align: 'left'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Altitude'
    },
    labels: {
      format: '{value} km'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Temperature'
    },
    labels: {
      format: '{value}°'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} km: {point.y}°C'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Temperature',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}
"""

# Define the main app function
def app():
      # Create a new Quasar page
    wp = jp.QuasarPage()
    # Add a header and a paragraph to the page
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = 'text-h1 text-center q-pa-md')
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")
    
     # Add a HighCharts component to the page with the options defined in chart_def
    hc = jp.HighCharts(a = wp, options = chart_def)

    # Update the x-axis categories and series data to display the monthly average ratings

    hc.options.xAxis.cateries = list(month_average.index)
    hc.options.series[0].data = list(month_average['Rating'])
    
    # Return the Quasar page
    return wp

# Start the JustPy server and pass the app function as a parameter
jp.justpy(app)