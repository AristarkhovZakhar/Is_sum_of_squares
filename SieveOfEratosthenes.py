def sieveOfEratosthenes(n): 
    sieve = [0] * (n + 1) 
    for i in range(n + 1):
        sieve[i] = 1 
    for i in range(2, floor(sqrt(n)) + 1):
        if sieve[i] == 1:
            j = 2
            while i * j <= n:
                sieve[i * j] = 0
                j = j + 1
    good_sieve = []
    for i in range(2, n + 1):
        if sieve[i] == 1 and i & 3 == 3:
            good_sieve.append(i)
    a = ",".join(map(str,sieveOfEratosthenes(100000)))
    return a

if __name__ == "__main__":
    print(sieveOfEratosthenes(10**6))
