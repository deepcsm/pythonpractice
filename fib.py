import math
import sys
def fib(n):
	a,b=0,1
	while n!=0:
		print b
		a,b=b,a+b
		n=n-1

if __name__=='__main__':
	fib(5)