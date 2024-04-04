# difference between two dates using portion 
import datetime as dt
from datetime import timedelta as td
import portion as p

start_date = dt.datetime(2024,1,16,0,00,00)
end_date = dt.datetime(2024,1,17,5,30,30)

night_interval = p.Interval()
main_interval = p.closed(start_date, end_date)
total_hours = td(0)

while start_date <= end_date+td(days=1):
    night_start = dt.datetime.combine(start_date.date(), dt.time(0))
    night_end = dt.datetime.combine(start_date.date(), dt.time(6))

    night_interval = night_interval.union(p.closed(night_start, night_end))

    start_date += td(days=1)

for i in main_interval - night_interval:
    total_hours += (i.upper - i.lower)

print(f"Total Difference Between Given Two Dates is :- ",total_hours)





# difference between two dates without using portion 
import datetime as dt

start_date = dt.datetime(2024,1,16,0,00,00)
end_date = dt.datetime(2024,1,17,5,30,30)

delta = dt.timedelta(days=1)
current_date = start_date

total_hours = dt.timedelta(0)
while current_date.date() <= end_date.date():
    night_start = dt.datetime.combine(start_date.date(),dt.time(0))
    night_end = dt.datetime.combine(start_date.date(),dt.time(6))

    current_date_max_time = dt.datetime.combine((current_date + delta).date(),dt.time(0))
    current_date_low_time = dt.datetime.combine(current_date.date(),dt.time(6))

    if (start_date.date() == end_date.date()) and (start_date >= night_end):
        total_hours += end_date - current_date

    elif (start_date.date() == end_date.date()) and (start_date < night_end):
        total_hours += end_date - current_date_low_time
        
    elif night_start <= current_date <= night_end:
        total_hours += (current_date_max_time - night_end)

    elif current_date.date() == end_date.date():
        if night_start <= end_date <= night_end:
            total_hours += (current_date_low_time - current_date_max_time)
        else:
            total_hours += (end_date - current_date_low_time)

    else:
        total_hours += (current_date_max_time - current_date_low_time)

    current_date += delta
    current_date = dt.datetime.combine(current_date.date(),dt.time(6))

print("Total Difference is :- ",total_hours)
