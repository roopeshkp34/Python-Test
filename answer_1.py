from datetime import date


f_date = date(2014, 6, 2)
l_date = date(2015, 7, 2)
delta = l_date - f_date
num_months = (l_date.year - f_date.year) * 12 + (l_date.month - f_date.month)
print(num_months)
if delta.days == 0 :
    print("The coast is 20RS")
elif delta.days > 0 and delta.days <= 31:
    cost=30*(delta.days)
    print("The coast is",cost)
elif delta.days > 31 and delta.days <=365:
    cost=30*(num_months)
    print("The coast is",cost)
else:
    print("The coast is 20000")
print(delta.days)