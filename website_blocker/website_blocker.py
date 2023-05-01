import time
from datetime import datetime as dt

host_path = '/etc/hosts/'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working hours...')
    else:
        print('It\'s fun hours... You are free to do whatever you want !')
    time.sleep(5)