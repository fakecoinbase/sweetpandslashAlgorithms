# 
# Solution to Project Euler problem 10

import eulerlib


# Call the sieve of Eratosthenes and sum the primes found.
def compute():
	ans = sum(eulerlib.list_primes(1999999))
	return str(ans)


if __name__ == "__main__":
	print(compute())