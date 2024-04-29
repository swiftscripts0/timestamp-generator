from datetime import datetime
import pytz 

# gets user input for timezone
while True:
  user_timezone = input("Enter your timezone (e.g., Europe/Paris, Australia/Sydney): ")
  # Check if the timezone is valid using pytz.all_timezones
  if user_timezone in pytz.all_timezones:
    break
  else:
    print("Invalid timezone. Please try again.")

# grabs current time in UTC
now_utc = datetime.now(pytz.utc)

# converts utc time to user's timezone
user_tz = pytz.timezone(user_timezone)
now_local = now_utc.astimezone(user_tz)

# formats date and time
date_input = f"{now_local.year}-{now_local.month:02d}-{now_local.day:02d}"
time_input = f"{now_local.hour:02d}:{now_local.minute:02d}"

# parses strings to date and time objects
date_object = datetime.strptime(date_input, "%Y-%m-%d")
time_object = datetime.strptime(time_input, "%H:%M")

# combines date and time
selected_date = datetime.combine(date_object, time_object.time())

# converting to timestamp
ts = str(int(selected_date.timestamp()))

# prints the current time into console
print(f'The current time is {now_local.hour}:{now_local.minute}')

# prints the exact copy and paste in the console
print(f'<t:{ts}:t>')
