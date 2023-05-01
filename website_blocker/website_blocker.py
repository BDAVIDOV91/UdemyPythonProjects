import time
from datetime import datetime as dt

host_temp = 'hosts'
host_path = '/etc/hosts/'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com',
                'netflix.com', 'disneyplus.com', 'hbomax.com', 'zoro.to', 
                'www.netflix.com', 'www.disneyplus.com', 'www.hbomax.com', 'www.zoro.to']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working hours...')
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print('It\'s fun hours... You are free to do whatever you want !')
    time.sleep(5)