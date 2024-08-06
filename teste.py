import datetime
x = "01/02/2024 09:30"
b = datetime.datetime.strptime(x, "%d/%m/%Y %H:%M")
print(b)