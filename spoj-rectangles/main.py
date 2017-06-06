import math

n = int(input())

res = 0

for i in range(1, int(math.sqrt(n))+1):
	res = res + ( (n//i) - (i-1) )

print(res)