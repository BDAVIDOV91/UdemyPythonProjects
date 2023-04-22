from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template()

@app.route('/success-table', methods = ['POST'])
def success_table():
    return render_template()

@app.route('/download-file/')
def download():
    return send_file

if __name__== '__main__':
    app.run(debug = True)