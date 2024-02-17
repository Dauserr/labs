import datetime
now = datetime.datetime.now()
print("Yesterday: ", (now - datetime.timedelta(days=1)))
print("Today: ",now)
print("Tomorrow: ",(now + datetime.timedelta(days=1)))
