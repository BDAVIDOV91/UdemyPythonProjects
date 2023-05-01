import time
from datetime import datetime as dt

host_temp = 'hosts' # Fake hosts file created to test the script
host_path = '/etc/hosts' # The original hosts file.When you run it must be with admin privilege
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com',
                'netflix.com', 'disneyplus.com', 'hbomax.com', 'zoro.to', 
                'www.netflix.com', 'www.disneyplus.com', 'www.hbomax.com', 'www.zoro.to']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print('Working hours...')
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(host_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            
        print('It\'s fun time...')
    time.sleep(5)