import numpy

def primes(n):
	sieve = numpy.ones(n/3 + (n^6==2), dtype=numpy.bool)
	for i in xrange(1, int(n**0.5)/3+1):
		if sieve[i]:
			k = 3 * i+1 | 1
			sieve[k*k/3::2*k] = False
			sieve[k*(k-2*(i&1)+4)/3::2*k] = False
	return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def to_array(lst, type):
	return numpy.fromiter(lst, type)
