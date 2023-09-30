"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import typing

def primes(number_of_primes: int) -> typing.List[int]:
    primes = []

    i = 2
    while len(primes) < number_of_primes:
        if all([i % x != 0 for x in primes]):
            primes.append(i)

        i += 1

    return primes
