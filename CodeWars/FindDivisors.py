"""
Find Divisors

Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""

def divisors(n):
    lst = [d for d in range(2,n-1) if n%d == 0]
    if len(lst) == 0:
        return "{} is prime".format(n)
    return lst

	
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

	
def divisors(integer):
  divisors = filter(lambda x: integer % x == 0, range(2, integer // 2 + 1))
  return divisors if divisors else "{0} is prime".format(integer)

  
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n

	
def divisors(integer):
  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)	

  
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n  

	
divisors = lambda z: [i for i in range(2,z) if z % i == 0] or ("%d is prime" % z)