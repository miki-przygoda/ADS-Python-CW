import time
import unittest
from testModules import tests2 as tests

# Basic Solution A:

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):  # 2 and 3 are prime -- skips small numbers
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(5, limit, 6): # 2 and 3 are already checked - start from 5 -- 6k +/- 1
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def find_primes(n: int, binary_str: str):
    primes = set()
    length = len(binary_str)

    for i in range(length): # O(n^2) -- O(n^3) in total -- need to shorten this - make it better...
        for j in range(i + 1, length + 1):
            substring = binary_str[i:j]
            decimal_num = int(substring, 2)
            if decimal_num < n and is_prime(decimal_num):
                primes.add(decimal_num)

    sorted_primes = sorted(primes)
    if len(sorted_primes) < 6:
        return f"{', '.join(map(str, sorted_primes))}"
    else:
        first_three = sorted_primes[:3]
        last_three = sorted_primes[-3:]
        return f"{len(sorted_primes)}: {', '.join(map(str, first_three))}, ..., {', '.join(map(str, last_three))}"

class TestFindPrimes(unittest.TestCase): # uses the test cases - hard coded.

    up_to = 10 # all test cases

    def run_test_case(self, test_index):
        binary, n = tests[test_index]
        prime_list = find_primes(n, binary)
        self.assertGreater(len(prime_list), 0, f"Test {test_index} failed: No primes found")
        print(f"Test {test_index + 1} Done.")


    def tests(self):
        for i in range(self.up_to):
            start = time.time()
            self.run_test_case(i)
            print(find_primes(tests[i][1], tests[i][0]))
            print(f"Time taken for test {i + 1}: {time.time() - start:.6f} seconds\n")
