cases = int(input())

for case in range(cases):

	n = int(input())

	men = [int(x) for x in input().split()]
	women = [int(x) for x in input().split()]

	men.sort(reverse=True)
	women.sort(reverse=True)
	
	res = 0
	for i in range(n):
		res = res + men[i]*women[i]

	print(res)

