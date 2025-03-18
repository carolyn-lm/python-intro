import datetime

current_time = datetime.datetime.now()

print(current_time.strftime("%m/%d/%Y"))
print(current_time.strftime("%B %e, %Y"))
print(current_time.strftime("%l:%M %p"))