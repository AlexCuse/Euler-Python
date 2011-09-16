import EUtils as eu

def solve():
	p = eu.primes(200000)
	return p[10001 - 1]

print solve()
