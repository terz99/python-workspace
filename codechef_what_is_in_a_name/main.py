import sys
import os

if __name__ == '__main__':
	num_cases = int(input())

	while(num_cases):
		num_cases -= 1
		name = str(input())
		l = name.split(' ')

		res = ''
		for i in range(len(l)-1):
			res += l[i][0].upper() + '. '

		res += l[-1].capitalize()
		print(res)