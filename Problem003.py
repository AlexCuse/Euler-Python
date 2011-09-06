import numpy as np
import EUtils as eu

def solve():
	x = np.int64(600851475143)
	ps = eu.primes(int(np.sqrt(x)))
	return np.max([p for p in ps if x % p == 0])

print solve()
