from datetime import datetime
now : datetime = datetime.now()

print(f'{now:%Y-%m-%d %H:%M}')  # 2023-10-05 14:48
# over all date time in ymd and hr min format 
print(f'{now:%B %d, %Y}')       # October 05, 2023
# local date and month 
print(f'{now:%I:%M %p}')        # 02:48 PM
# time in hr min and am/pm format

