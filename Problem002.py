import numpy as np
import EUtils as eu

def fib(n):
	a, b = 0, 1
	while a < n:
		yield a
		a, b = b, a + b

def solve():
	fibs = eu.to_array(fib(4000000), int)
	return np.sum(np.select([fibs % 2 == 0], [fibs]))

print solve()
