from  datetime import datetime

now = datetime.now()

date_input = f"{now.year}-{now.month:02d}-{now.day:02d}"
time_input = f"{now.hour:02d}:{now.minute:02d}"

date_object = datetime.strptime(date_input, "%Y-%m-%d")
time_object = datetime.strptime(time_input, "%H:%M")


selected_date = datetime.combine(date_object, time_object.time())
ts = str(int(selected_date.timestamp()))

print(f'The current time is {now.hour}:{now.minute}')

print(f'<t:{ts}:t>')