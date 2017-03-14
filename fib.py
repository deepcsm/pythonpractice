import math
import sys
def fib(n):
	"""This is a function to print the fibonaci series for the given input """
	a,b=0,1
	while n!=0:
		print b
		a,b=b,a+b
		n=n-1

if __name__=='__main__':
	n=int(input('Please enter the number for which the Fib series to be printed'))
	if n <1:
		print ("Please enter a Postive number greater than o")
		sys.exit()
	else:
		fib(n)