import justpy as jp 
import pandas
from datetime import datetime
from pytz import utc

# read data from csv file
data = pandas.read_csv('reviews.csv', parse_dates = ['Timestamp'])

# group data by course name and count the number of ratings for each course
share = data.groupby(['Course Name'])['Rating'].count()

# HighCharts configuration in JSON format
chart_def =  """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in May, 2020',
        align: 'left'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 70.67,
            sliced: true,
            selected: true
        }, {
            name: 'Edge',
            y: 14.77
        },  {
            name: 'Firefox',
            y: 4.86
        }, {
            name: 'Safari',
            y: 2.63
        }, {
            name: 'Internet Explorer',
            y: 1.53
        },  {
            name: 'Opera',
            y: 1.40
        }, {
            name: 'Sogou Explorer',
            y: 0.84
        }, {
            name: 'QQ',
            y: 0.51
        }, {
            name: 'Other',
            y: 2.6
        }]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = 'text-h1 text-center q-pa-md')
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")
    
    # add a HighCharts component to the page
    hc = jp.HighCharts(a = wp, options = chart_def)
    
    # format the data for HighCharts
    hc_data = [{'name': v1, 'y': v2} for v1, v2 in zip(share.index, share)]
    
    # set the data for the HighCharts component
    hc.options.series[0].data = hc_data
    
    return wp

# start the web application
jp.justpy(app)