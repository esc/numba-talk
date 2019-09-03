import numpy as np
import numba as nb

@nb.njit  # simply add the njit decorator
def primes(max=100000):
    numbers = np.ones(max, dtype=np.uint8)  # initialize the boolean sieve
    for i in range(2, max):
        if numbers[i] == 0:  # has previously been crossed off
            continue
        else:  # it is a prime, cross off all mutiples
            x = i + i
            while x < max:
                numbers[x] = 0
                x += i
    # return all primes, as indicated by all boolean positions that are one
    return np.nonzero(numbers)[0][2:]
