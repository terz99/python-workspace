n = int(input())

while n != -1:

	a = []

	for i in range(n):
		tmp_int = int(input())
		a.append(tmp_int)

	a_sum = sum(a)

	if a_sum%n != 0:
		print("-1")
	else:
		mod = a_sum//n
		res = 0
		for elem in a:
			res = res + abs(mod-elem)

		print(res//2)

	n = int(input())