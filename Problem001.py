import numpy as np

def solve(): 
	arr = np.arange(1000)
	nums = np.select([arr % 3 == 0, arr % 5 == 0], [arr, arr])
	return np.sum(nums)
print solve()
