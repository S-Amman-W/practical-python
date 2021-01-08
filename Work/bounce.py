# bounce.py
#
# Exercise 1.5
ball = 100
count = 1
while count < 11:
    ball = ball * 3 / 5
    print(count, round(ball, 4))
    count = count + 1
