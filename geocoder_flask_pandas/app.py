from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas as pd
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success-table', methods = ['POST'])
def success_table():
    global filename
    if request.method == 'POST':
        file = request.files['file']
        try:
            df = pd.read_csv(file)
            gc = Nominatim(user_agent='Legit Geocoder', scheme = 'http')
            df["coordinates"] = df["Address"].apply(gc.geocode)
            df['Latitude'] = df['coordinates'].apply(lambda x: x.latitude if x != None else None)
            df['Longitude'] = df['coordinates'].apply(lambda x: x.longitude if x != None else None)
            df = df.drop('coordinates', axis = 1, inplace = True)
            filename = datetime.datetime.now().strftime('uploeads/%Y-%m-%d-%H-%M-%S-%f' + '.csv')
            df.to_csv(filename, index=None)
            return render_template('index.html', text = df.to_html(), btn = 'download.html')
        except Exception as e:
            return render_template("index.html", text=str(e))

@app.route('/donwload-file/')
def download():
    return send_file(filename, attachment_file = 'yourfile.csv', as_attachment = True)

if __name__== '__main__':
    app.run(debug = True, port = 5005) # In my case port :5000 was busy so we can switch ports