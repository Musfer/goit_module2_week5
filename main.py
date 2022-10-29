from math import sqrt
from collections import Counter
import time
import random
from multiprocessing import Pool, cpu_count


def primes_dict(n: int):
    """finds all prime factors and count them into the dictionary
        i.e. primes_dict(12) = {2: 2, 3: 1})"""
    prime_div = []
    i = 2
    while i < sqrt(n) + 1:
        if n % i == 0:
            prime_div.append(i)
            n = n // i
        else:
            i += 1
    if n != 1:
        prime_div.append(n)
    return Counter(prime_div)


def factorize_num(n: int):
    primes = primes_dict(n)
    result = [1]
    for prime, power in primes.items():
        new_numbers = []
        for i in range(1, power+1):
            for x in result:
                new_numbers.append(x * prime**i)
        result += new_numbers
    return sorted(result)


def factorize(lst: [int]):
    return [factorize_num(x) for x in lst]


if __name__ == '__main__':

    # tests
    print("Simple test")
    a, b, c, d = factorize([128, 255, 99999, 10651060])
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    print("done")
    # end of test

    m = 20
    numbers = [random.randint(1, 100000000000000) for _ in range(m)]

    print(f"\nTesting on big numbers: {numbers}")
    print("\nFactorizing without multiprocessing")
    start = time.time()
    result1 = factorize(numbers)
    end = time.time()
    print(f"done in {end-start} seconds")

    n_processes = cpu_count()
    # n_processes = cpu_count() // 2
    # n_processes = 12
    print(f"\nMultiprocessing on {n_processes} core(s)")
    start = time.time()
    with Pool(processes=n_processes) as pool:
        result2 = pool.map(factorize_num, numbers)
    end = time.time()
    print(f"done in {end-start} seconds")

    if result1 == result2:
        print("\nResults match")
    else:
        print("\nSomething went wrong. Results do not match.")
