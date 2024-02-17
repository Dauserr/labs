import datetime
x = datetime.datetime(2023,6,1,15,55,45)
y = datetime.datetime(2024,1,2,14,15,20)

overall = 0
years = abs(int(x.strftime("%Y"))-int(y.strftime("%Y")))*365*24*60*60
overall+=years
months = abs(int(x.strftime("%m"))-int(y.strftime("%m")))*30*24*60*60
overall+=months
days = abs(int(x.strftime("%d"))-int(y.strftime("%d")))*24*60*60
overall+=days
hours = abs(int(x.strftime("%H"))-int(y.strftime("%H")))*60*60
overall+=hours
mins = abs(int(x.strftime("%M"))-int(y.strftime("%M")))*60
overall+=mins
secs = abs(int(x.strftime("%S"))-int(y.strftime("%S")))
overall+=secs


print(overall)
