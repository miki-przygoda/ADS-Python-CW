import time
import unittest
import numpy as np
from testModules import tests2 as tests # import from a file called testModules.py

substring_cache = {} # A cache used to store the decimal equivalent of the binary substring

def miller_rabin(n: int, k: int = 5) -> bool:
    """
    Miller-Rabin primality test
    n: number to test
    k: number of rounds (higher k = higher accuracy)
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = int(np.random.randint(2, n - 1))  # Convert numpy.int64 to Python int
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def is_prime(n: int) -> bool:
    if n < 2:  # 0 and 1 are not prime
        return False
    if n in (2, 3):  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # skips even numbers and multiples of 3
        return False
    
    # Use Miller-Rabin for larger numbers (n > 6)
    if n > 6:
        return miller_rabin(n)
    
    # For smaller numbers, use the original deterministic method
    limit = int(np.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def process_section(section: str, n: int) -> set:
    primes = set()  # A set to store prime numbers found in the section
    
    # Convert section to numpy array for faster processing
    section_array = np.array([int(bit) for bit in section])
    
    for i in range(len(section)):
        if section[i] == '0':  # Skip if starting with 0, since it will not be a prime
            continue
            
        # Use numpy for faster binary to decimal conversion
        num = 0
        for j in range(i, len(section)):
            num = (num << 1) | int(section_array[j])  # Ensure we're using Python int
            if num >= n:  # Stop if number exceeds limit
                break
                
            if num in substring_cache:  # Check cache first to avoid redundant processing
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

    if test_index <= 3:    # Calculate section size and overlap
        num_sections = 2
    if test_index <= 5:
        num_sections = 5
    else:
        num_sections = 7

    section_size = length // num_sections
    overlap_size = 51  # Size of overlap between sections to catch primes spanning boundaries

    sections = []     # Create sections with overlap in case of primes spanning boundaries
    for i in range(num_sections):
        start = i * section_size
        end = start + section_size + overlap_size if i < num_sections - 1 else length
        section = binary_str[start:end]
        sections.append(section)

    for section in sections:
        primes.update(process_section(section, n))

    sorted_primes = sorted(primes) # Sort the primes for display - smallest to largest
    prime_count = len(sorted_primes)

    # Format the output based on the number of primes found
    if prime_count < 6:
        return f"{', '.join(map(str, sorted_primes))}"
    else:
        first_three = sorted_primes[:3]
        last_three = sorted_primes[-3:]
        return f"{prime_count}: {', '.join(map(str, first_three))} ... {', '.join(map(str, last_three))}"

def test_with_detailed_prints(binary_str: str, n: int, test_index: int = -1):
    start = time.time()
    formatted_output = find_primes(n, binary_str, test_index)
    elapsed = time.time() - start

    print(f"Formatted output: {formatted_output}")
    print(f"Time taken: {elapsed:.6f} seconds\n")

class TestFindPrimes(unittest.TestCase): # uses the test cases - hard coded.

    up_to = 10 # all test cases

    def test_with_numbers(self):
        for i in range(self.up_to):
            binary, n = tests[i]
            print(f"Test: {i + 1}")
            test_with_detailed_prints(binary, n)

if __name__ == '__main__':
    unittest.main()