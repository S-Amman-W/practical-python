# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f)
    total = 0
    for line in f:
        rows = line.split(',')
        total = total + (float(rows[1]) * float(rows[2]))
    return round(total, 2))
    
print('Total cost', portfolio_cost('Data/portfolio.csv'))

