import time
import unittest
from testModules import tests2 as tests

# Expected_Results = [
# 1,"15: 2, 3, 5 ... 269, 2153, 17231"
# 2,"28: 2, 3, 5 ... 10729, 17231, 85837"
# 3,"7: 3, 7, 31 ... 8191, 131071, 524287"
# 4,"44: 2, 3, 5 ... 5571347, 41577089, 55398449"
# 5,"52: 2, 3, 5 ... 84087683, 3920234023, 5625434161"
# 6,"64: 2, 3, 5 ... 2724796139969, 5841981288761, 45810224399911"
# 7,"71: 2, 3, 5 ... 45810224399911, 7435453988964809, 18946016916092977"
# 8,"76: 2, 3, 5 ... 45810224399911, 7435453988964809, 18946016916092977"
# 9,"81: 2, 3, 5 ... 7435453988964809, 18946016916092977, 378518838354150661"
# 10,"89: 2, 3, 5 ... 7435453988964809, 18946016916092977, 378518838354150661"
# ]

# -- Instructions and description of the task / structures to be used
"""
Your task is to write a Python program that finds all unique prime numbers hidden within a
given binary string, and less than a given integer number N.
For example, given the binary string "0110" and the number 5, we can extract multiple
substrings, such as "0", "1", "11", "10", "110"… Converting these binary substrings into their
decimal equivalents gives the numbers 0, 1, 2, 3, 6, and so on. Among these, we identify the
prime numbers that are less than a given value 5. In this case, the prime numbers are 2
(decimal equivalent of binary string "10") and 3 (decimal equivalent of binary string "11")
after removing duplicates. So the output is "2: 2, 3"
We need to print all the prime numbers, if fewer than 6 prime numbers are found.
However, if 6 or more prime numbers are found, it should display only the first three
smallest primes and the last three largest ones.
"""

# Expected_Results = [§
# 1,"15: 2, 3, 5 ... 269, 2153, 17231"
# 2,"28: 2, 3, 5 ... 10729, 17231, 85837"
# 3,"7: 3, 7, 31 ... 8191, 131071, 524287"
# 4,"44: 2, 3, 5 ... 5571347, 41577089, 55398449"
# 5,"52: 2, 3, 5 ... 84087683, 3920234023, 5625434161"
# 6,"64: 2, 3, 5 ... 2724796139969, 5841981288761, 45810224399911"
# 7,"71: 2, 3, 5 ... 45810224399911, 7435453988964809, 18946016916092977"
# 8,"76: 2, 3, 5 ... 45810224399911, 7435453988964809, 18946016916092977"
# 9,"81: 2, 3, 5 ... 7435453988964809, 18946016916092977, 378518838354150661"
# 10,"89: 2, 3, 5 ... 7435453988964809, 18946016916092977, 378518838354150661"
# ]

substring_cache = {} # A cache used to store the decimal equivalent of the binary substring


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2: # 0 and 1 are not prime
        return False
    if n in (2, 3): # 2 and 3 are prime -- skips small numbers
        return True
    if n % 2 == 0 or n % 3 == 0: # skips even numbers and multiples of 3
        return False
    limit = int(n ** 0.5) + 1 # limit to check for prime numbers
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0: # skips multiples of 5 and 7
            return False # not a prime number
    return True # is a prime number

def process_section(section: str, n: int) -> set:
    """Process a section of the binary string to find primes."""
    primes = set()

    for i in range(len(section)):
        # Skip if starting with 0 since we don't want leading zeros
        if section[i] == '0':
            continue
        num = 0  # Rolling binary-to-decimal conversion
        for j in range(i, len(section)):
            num = (num << 1) | int(section[j])  # Convert binary to decimal
            if num >= n:  # Stop if number exceeds limit
                break
            # Check cache first to avoid redundant processing
            if num in substring_cache:
                is_prime_cached = substring_cache[num]
            else:
                is_prime_cached = is_prime(num)
                substring_cache[num] = is_prime_cached

            if is_prime_cached:
                primes.add(num)
    return primes

def find_primes(n: int, binary_str: str, test_index: int):
    primes = set()
    length = len(binary_str)
    test_index =+ 1

    if test_index <= 5:
        num_sections = 3
        section_size = length // num_sections
        sections = [binary_str[i * section_size:(i + 1) * section_size] for i in range(num_sections)]
        sections[-1] += binary_str[num_sections * section_size:]  # Add remaining part to the last section
    else:
        num_sections = 6
        section_size = length // num_sections
        sections = [binary_str[i * section_size:(i + 1) * section_size] for i in range(num_sections)]
        sections[-1] += binary_str[num_sections * section_size:]  # Add remaining part to the last section

    # Process each section sequentially
    for section in sections:
        primes.update(process_section(section, n))

    # Sort the primes for display
    sorted_primes = sorted(primes)
    prime_count = len(sorted_primes)

    # Format the output based on the number of primes found
    if prime_count < 6:
        return f"{', '.join(map(str, sorted_primes))}"
    else:
        first_three = sorted_primes[:3]
        last_three = sorted_primes[-3:]
        return f"{', '.join(map(str, first_three))} ... {', '.join(map(str, last_three))} (Total primes: {prime_count})"


def test_with_detailed_prints(binary_str: str, n: int, test_index: int = -1):
    """Runs a detailed test case with prints of all primes and formatted output."""
    print(f"Testing with binary string: {binary_str[:50]}... (truncated)" if len(
        binary_str) > 50 else f"Testing with binary string: {binary_str}")
    print(f"Hard limit (N): {n}")

    start = time.time()
    formatted_output = find_primes(n, binary_str, test_index)
    elapsed = time.time() - start

    print(f"Formatted output: {formatted_output}")
    print(f"Time taken: {elapsed:.6f} seconds\n")


class TestFindPrimes(unittest.TestCase): # uses the test cases - hard coded.

    up_to = 10 # all test cases

    def run_test_case(self, test_index):
        binary, n = tests[test_index]
        prime_list = find_primes(n, binary, test_index)
        self.assertGreater(len(prime_list), 0, f"Test {test_index} failed: No primes found")
        # print(f"Test {test_index + 1} Done.")

    def test_with_numbers(self):
        for i in range(self.up_to):
            binary, n = tests[i]
            print(f"Test: {i + 1}")
            test_with_detailed_prints(binary, n)

    # def test(self):
    #     for i in range(self.up_to):
    #         self.run_test_case(i)

    # def test_average(self):
    #     """Test to calculate the average time taken for each test case."""
    #     number_of_repeats = 100
    #     time_for_each = []
    #     for _ in range(number_of_repeats):
    #         for n in range(self.up_to):
    #             start = time.time()
    #             self.run_test_case(n)
    #             elapsed = time.time() - start
    #             time_for_each.append(elapsed)
    #     print(f"Average time taken for each test case: {sum(time_for_each) / number_of_repeats:.6f} seconds")



if __name__ == '__main__':
    unittest.main()