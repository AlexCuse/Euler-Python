import numpy as np
import EUtils as eu

def all_products_between(start, stop):
	for n in range(start, stop):
		for o in range(start, stop):
			out = n * o
			yield out

def palindrome(num):
	s = str(num)
	return s == s[::-1]

def solve():
	arr = np.fromiter(all_products_between(100, 999), int)
	distinct = np.unique(arr)
	filtered = [n for n in distinct if palindrome(n)] 
	return np.max(filtered)
	
print solve()
