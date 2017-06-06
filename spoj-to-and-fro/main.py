def rev(l):
	if(len(l) <= 1):
		return l
	return rev(l[1:]) + l[0]

n = int(input())

while n != 0:

	enc = str(input())

	s = ""
	l = []
	cnt = 0
	for letter in enc:
		if(cnt == n):
			l.append(s)
			s = ""
			cnt = 0

		cnt += 1
		s = s + letter

	l.append(s)

	for i in range(1, len(l), 2):
		l[i] = rev(l[i])

	res = ""

	for i in range(n):
		for j in range(len(l)):
			res = res + l[j][i]

	print(res)
	n = int(input())