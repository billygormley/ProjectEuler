sumSq = 0
sum1 = 0

for i in range(1,101):
    sumSq += i**2

for j in range(1,101):
    sum1 += j

sum1Sq = sum1**2

diff = sum1Sq - sumSq

print(diff)
