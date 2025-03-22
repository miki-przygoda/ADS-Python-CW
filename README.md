# 🔢 Prime Finder in Binary Strings

This project implements a series of Python algorithms to extract and analyze **unique prime numbers** from binary strings.  
Originally developed for my **Algorithms & Data Structures module** at the University of Greenwich, the project evolved into a performance-focused exploration of string manipulation, primality testing, and memory-efficient caching.

---

## 🧠 Problem Summary

Given a binary string (e.g., `"0110"`) and a threshold integer `N` (e.g., `5`), the program:

1. Extracts all possible **binary substrings**
2. Converts them into **decimal integers**
3. Identifies **unique primes** below `N`
4. Formats the output based on how many primes were found
5. Cannot use any external libraries

---

## 🖥️ Output Format

- **If fewer than 6 prime numbers** are found: show *all* primes in ascending order  
- **If 6 or more primes** are found: show the **first 3**, **last 3**, and a count summary  
- Example: `2 3 5 ... 89 97 101 (Total: 45 primes)`

---

## 🧩 Project Structure

```
├── basicA.py         # Naive O(n³) brute-force implementation
├── main.py           # Optimized solution with caching and sectioning
├── draft3.py         # Experimental implementations and optimization trials
├── testModules.py    # Unit tests using Python’s built-in unittest module
└── README.md
```

---

## ⚙️ Implementations

### 🐢 Basic Implementation (`basicA.py`)
A direct brute-force method:
- Triple-nested loop over substrings
- Converts and checks all values
- No reuse of previously tested primes

### ⚡ Optimized Implementation (`main.py`)
A refined and scalable version:
- **Substring caching** for reuse
- **Efficient primality testing**
- **Section-based chunking** of input for parallel-ready logic
- Optimized binary-to-decimal conversion

### 🧪 Drafts & Experiments (`draft3.py`)
Contains older versions and exploratory strategies for optimization.

---

## ✅ Testing

Run with:

```bash
python main.py
```

Or run test cases directly:

```bash
python -m unittest testModules.py
```

Tests validate:
- Correct prime identification
- Output formatting
- Edge case handling

---

## 🚀 Performance Focus

Compared to the naive solution, the optimized version shows massive improvements on:
- Long binary strings
- High threshold `N`
- Reuse of sub-calculations via caching
- Lowered time complexity from O(n³) to near-linear for many practical cases

---

## ✍️ Author

**Mikolaj Mikuliszyn**  
1st Year BSc Computer Science & Artificial Intelligence  
University of Greenwich, London  
🔗 [GitHub Profile](https://github.com/miki-przygoda)

---

## ⚠️ Disclaimer

This project was originally submitted for coursework.  
It is shared here for educational and portfolio purposes only.
