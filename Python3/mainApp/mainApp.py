import time
from Exercises import *


def main():
    print("Finding Primes...")

    ex = Exercises()
    print(ex.find_n_primes(5))
    print(ex.find_n_primes(10))
    print(ex.find_n_primes(15))

    print(ex.fibonacci(15))
    print(ex.fibonacci(5))
    print(ex.fibonacci(3))
    print(ex.fibonacci(2))
    print(ex.fibonacci(1))

    print("Largest Palindrone in EDEFABCBAYT")
    print("Final Result: " + ex.find_largest_palindrone("EDEFABCBAYT"))

    print("K most frequent elements")
    tstart = time.time()
    print(ex.get_common_elements(2, [1, 2, 3, 2, 4, 6, 6, 2]))
    print(ex.get_common_elements(2, [1, 6, 3, 2, 4, 6, 6, 2]))
    print(ex.get_common_elements(4, [1, 1, 1, 6, 4, 2, 4, 6, 6, 2]))
    print(ex.get_common_elements(4, [4, 6, 6, 2, 4, 4, 6, 6, 2, 1]))
    tend = time.time()
    print(tend - tstart)

    print("K most frequent elements V2")
    tstart = time.time()
    print(ex.get_common_elements_v2(2, [1, 2, 3, 2, 4, 6, 6, 2]))
    print(ex.get_common_elements_v2(2, [1, 6, 3, 2, 4, 6, 6, 2]))
    print(ex.get_common_elements_v2(4, [1, 1, 1, 6, 4, 2, 4, 6, 6, 2]))
    print(ex.get_common_elements_v2(4, [4, 6, 6, 2, 4, 4, 6, 6, 2, 1]))
    tend = time.time()
    print(tend - tstart)

    print("Ricky Version - K most frequent elements")
    print(ex.ricky_find_max_elements_v2( [1, 2, 3, 2, 4, 6, 6, 2]))
    #print(ex.ricky_find_max_elements_v2(2, [1, 6, 3, 2, 4, 6, 6, 2]))
    #print(ex.ricky_find_max_elements_v2(3, [1, 1, 1, 6, 4, 2, 4, 6, 6, 2]))
    #print(ex.ricky_find_max_elements_v2(3, [4, 6, 6, 2, 4, 4, 6, 6, 2, 1]))


if __name__ == "__main__":
    main()
