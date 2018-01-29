from collections import defaultdict
import math

#check if n is prime divisor
def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    for i in range(3,int(math.sqrt(n)) + 1,2):
        if n%i == 0:
            return False
    return True

#prime divisor of each number
reduce = defaultdict(list)

def map(x):
    output = []
    for i in range(2, x):
        if isPrime(i) and x%i == 0:
            output.append(i)
    return output

integerList = [15, 21, 24, 30, 49]

# Print integers and its prime divisors
for n in integerList:
    print "Integer:", n
    primeDivisors = map(n)

    print "Prime divisors:", primeDivisors
    for key in primeDivisors:
        reduce[key].append(n)

# Print prime divisors and the sum of the integers mapped to it
for key, values in reduce.items():
    print "Prime divisor and sum:", key, ",", sum(values)