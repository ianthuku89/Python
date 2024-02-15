import datetime
import pytz
from datetime import timedelta
from pytz import timezone

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

# Corrected usage:
# Use datetime.datetime objects for start and stop arguments
# Instead of datetime, use datetime.datetime
# Adjust the timedelta to represent 6 hours
for d in date_range(datetime.datetime(2012, 10, 1), datetime.datetime(2012, 10, 30), timedelta(hours=24)):
    print(d)

#Converting strings  to datetime objects
text = ('2002-10-29')
y = datetime.datetime.strptime(text, '%Y-%m-%d')
print(y)

#Manipulating dates involving timezones
d = datetime.datetime(2012,10,29,9,30,0)
central = timezone('US/Central')
loc_d =  central.localize(d)
print(loc_d)
#Convert to asian time
asian_t = loc_d.astimezone(timezone('Asia/Kolkata'))
print("Time: ", asian_t)
#Convert to utc
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
   