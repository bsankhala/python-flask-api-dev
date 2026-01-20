from datetime import datetime, timedelta
import pytz

event_input = input("Enter the event date and time (YYYY-MM-DD HH:MM:SS): ")
event_dt = datetime.strptime(event_input, "%Y-%m-%d %H:%M:%S")
now = datetime.now()

if event_dt < now:
    print("Event already passed!")
else:
    remaining = event_dt - now
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    
    print(f"Time remaining to event: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    now_ts = now.timestamp()
    event_ts = event_dt.timestamp()
    print(f"Current timestamp: {now_ts}")
    print(f"Event timestamp: {event_ts}")

    tz = pytz.timezone('Asia/Kolkata')
    event_dt_tz = pytz.utc.localize(event_dt).astimezone(tz)
    print("Event time in Asia/Kolkata timezone:", event_dt_tz.strftime("%Y-%m-%d %H:%M:%S"))
