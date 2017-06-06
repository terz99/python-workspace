from sys import stdin, stdout

input_list = input().split()
a = int(input_list[0])
b = int(input_list[1])
c = int(input_list[2])

while not (a == 0 and b == 0 or c == 0):

	if b-a == c-b:
		print('AP {}'.format(c + (c-b)))
	else:
		print('GP {}'.format(c*(c//b)))

	input_list = input().split()
	a = int(input_list[0])
	b = int(input_list[1])
	c = int(input_list[2])