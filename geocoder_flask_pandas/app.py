from flask import Flask, render_template, request, send_from_directory
from geopy.geocoders import Nominatim
import pandas as pd
import datetime
import os

app = Flask(__name__)

upload_directory = os.path.abspath('uploads')

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
            df_coordinates = df.drop('coordinates', axis = 1)
            filename = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f' + '.csv')
            file_path = os.path.join(upload_directory, filename)
            df_coordinates.to_csv(file_path, index=None)
            return render_template('index.html', text = df_coordinates.to_html(), btn = 'download.html')
        except Exception as e:
            return render_template("index.html", text=str(e))

@app.route('/download/<filename>')
def download_file(filename):
    print("Download function called with filename:", filename)

    return send_from_directory(directory = upload_directory, filename = filename.split('/')[-1], as_attachment = True)

if __name__== '__main__':
    app.run(debug = True, port = 5005) # In my case port :5000 was busy so we can switch ports