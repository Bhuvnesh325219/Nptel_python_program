

from datetime import datetime as dt
import datetime
import calendar

import pytz

#tz=pytz.timzone('Singapore')
#print(dt.now(tz))

print(dt.now())
print(len(pytz.all_timezones))
print(pytz.all_timezones)


#year,month,day
print(calendar.weekday(2021,8,18))


yy=2017
mm=11
dd=17

print(calendar.month(yy,mm))
print(datetime.datetime.utcnow())
