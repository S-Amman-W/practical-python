# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f)
total = 0
for line in f:
    rows = line.split(',')
    total = total + (float(rows[1]) * float(rows[2]))

print('Total cost', (round(total, 2)))