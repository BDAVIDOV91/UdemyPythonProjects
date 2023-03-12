from datetime import date


today = date.today()
aleks_birthday = date(today.year, 5, 8)
if aleks_birthday < today:
    aleks_birthday = aleks_birthday.replace(year = today.year + 1)
time_till_birthday = abs(aleks_birthday - today)

# transform (PARSE) timetillbirthday.days to string (str)
print(str(time_till_birthday.days) +  ' days')