"""
Sum NTH term

Your task is to write a function which returns the sum of following series upto nth term(parameter).
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
"""

series_sum = lambda n: '%1.2f' % sum(map(lambda x : 1 / (1 + 3 * x), range(n)))


def series_sum(n):
    z = []
    for x in range(n):
        z.append(1 / (1 + 3 * x))
    return '%1.2f' % sum(z)

	
def series_sum(n):
    return '%.2f' % sum(1.0 / i for i in xrange(1, 3 * n, 3))	

	
def series_sum(n):
  return "%.2f" % sum([1.0 / (3 * i + 1) for i in range(n)])	

  
def series_sum(n):
    return '%.2f' % sum(1.0 / i for i in xrange(1, 3 * n, 3))  
 
  
series_sum = lambda n: '%1.2f' % sum(1 / i for i in xrange(1, 3 * n, 3))  