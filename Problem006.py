def sum_squares (limit) :
	sum = 0
	for n in range(1, limit + 1):
		sum += n * n
	return sum

def square_sum (limit) :
	sum = 0
	for n in range(1, limit + 1):
		sum += n
	return sum * sum

def solve():
	return abs(sum_squares(100) - square_sum(100))

print solve()
