n = 21
prime_factors = []

def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True



for i in range(2, n+1):
    if n%i == 0:
        if(isPrime(i)):
            prime_factors.append(i)
print(prime_factors)