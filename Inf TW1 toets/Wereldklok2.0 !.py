import datetime
import pytz

tz = pytz.timezone('Europe/Moscow')
ct = datetime.datetime.now(tz=tz)
print(ct)
