# kintsugi-stack-dsa-python


> “Code is read much more often than it is written.” — Guido van Rossum

- Author: [Kintsugi-Programmer](https://github.com/kintsugi-programmer)

![alt text](image.png)

> Disclaimer: The content presented here is a curated blend of my personal learning journey, experiences, open-source documentation, and invaluable knowledge gained from diverse sources. I do not claim sole ownership over all the material; this is a community-driven effort to learn, share, and grow together.

## Table of Contents
- [kintsugi-stack-dsa-python](#kintsugi-stack-dsa-python)
  - [Table of Contents](#table-of-contents)
  - [0. Introduction](#0-introduction)
    - [0.1. Why Learn Data Structures and Algorithms?](#01-why-learn-data-structures-and-algorithms)
    - [0.2. Course Topics Covered](#02-course-topics-covered)
  - [1. Introduction to Algorithms](#1-introduction-to-algorithms)
    - [1.1. What is an Algorithm?](#11-what-is-an-algorithm)
    - [1.2. Three Goals of This Course](#12-three-goals-of-this-course)
    - [1.3. Important Philosophy](#13-important-philosophy)
    - [1.4. Example: Find Minimum Algorithm](#14-example-find-minimum-algorithm)
    - [1.5. Algorithm Must Be Finite](#15-algorithm-must-be-finite)
    - [1.6. Pseudocode: Mystery Algorithm (Reverse String)](#16-pseudocode-mystery-algorithm-reverse-string)
    - [1.7. Simple Algorithms Example: Sum](#17-simple-algorithms-example-sum)
    - [1.8. Simple Algorithms Example: Find Longest String](#18-simple-algorithms-example-find-longest-string)
  - [2. Math for Programmers](#2-math-for-programmers)
    - [2.1. Exponents](#21-exponents)
    - [2.2. Exercise: Get Estimated Spread (Social Litics)](#22-exercise-get-estimated-spread-social-litics)
    - [2.3. Geometric Sequences](#23-geometric-sequences)
    - [2.4. Exercise: Get Follower Prediction (Geometric Growth)](#24-exercise-get-follower-prediction-geometric-growth)
    - [2.5. Nonlinear Growth](#25-nonlinear-growth)
    - [2.6. Logarithms](#26-logarithms)
    - [2.7. Factorials](#27-factorials)
  - [3. Big O Analysis](#3-big-o-analysis)
    - [3.1. What is Big O?](#31-what-is-big-o)
    - [3.2. Constant Time: O(1)](#32-constant-time-o1)
    - [3.3. Linear Time: O(n)](#33-linear-time-on)
    - [3.4. Logarithmic Time: O(log n)](#34-logarithmic-time-olog-n)
    - [3.5. Linearithmic Time: O(n log n)](#35-linearithmic-time-on-log-n)
    - [3.6. Quadratic Time: O(n²)](#36-quadratic-time-on)
    - [3.7. Two Variables: O(n·m)](#37-two-variables-onm)
    - [3.8. Exponential Time: O(2^n)](#38-exponential-time-o2n)
    - [3.9. Factorial Time: O(n!)](#39-factorial-time-on)
    - [3.10. Big O Complexity Chart (Best to Worst)](#310-big-o-complexity-chart-best-to-worst)
    - [3.11. Important: Constants Don't Matter](#311-important-constants-dont-matter)
    - [3.12. Find Max (O(n))](#312-find-max-on)
    - [3.13. Find Full Name (O(n²))](#313-find-full-name-on)
    - [3.14. Average Brand Followers (O(n·m))](#314-average-brand-followers-onm)
    - [3.15. Find Last Name (O(1))](#315-find-last-name-o1)
    - [3.16. Binary Search (O(log n)) — Full Steps](#316-binary-search-olog-n--full-steps)
  - [4. Sorting Algorithms](#4-sorting-algorithms)
    - [4.1. Built-in Sorting (Python)](#41-built-in-sorting-python)
    - [4.2. Exercise: Vanity Sort (Social Litics)](#42-exercise-vanity-sort-social-litics)
    - [4.3. Why Learn Sorting?](#43-why-learn-sorting)
    - [4.4. Bubble Sort](#44-bubble-sort)
    - [4.5. Merge Sort](#45-merge-sort)
    - [4.6. Insertion Sort](#46-insertion-sort)
    - [4.7. Quicksort](#47-quicksort)
    - [4.8. Sorting Quiz Summary](#48-sorting-quiz-summary)
  - [5. Exponential Time](#5-exponential-time)
    - [5.1. Polynomial vs Exponential](#51-polynomial-vs-exponential)
    - [5.2. Fibonacci Sequence](#52-fibonacci-sequence)
    - [5.3. Power Set](#53-power-set)
    - [5.4. Chapter 5 Quiz](#54-chapter-5-quiz)
  - [6. Introduction to Data Structures](#6-introduction-to-data-structures)
    - [6.1. What are Data Structures?](#61-what-are-data-structures)
    - [6.2. Exercise: Count Markers (Locked In)](#62-exercise-count-markers-locked-in)
    - [6.3. Exercise: Last Work Experience](#63-exercise-last-work-experience)
    - [6.4. Lists (Arrays)](#64-lists-arrays)
    - [6.5. Tuples](#65-tuples)
  - [7. Stacks](#7-stacks)
    - [7.1. What is a Stack?](#71-what-is-a-stack)
    - [7.2. Stack Operations](#72-stack-operations)
    - [7.3. Stack Implementation](#73-stack-implementation)
    - [7.4. Real-World Uses](#74-real-world-uses)
    - [7.5. Example: Balanced Parentheses](#75-example-balanced-parentheses)
  - [8. Queues](#8-queues)
    - [8.1. What is a Queue?](#81-what-is-a-queue)
    - [8.2. Queue Operations](#82-queue-operations)
    - [8.3. Queue Implementation (Array-Based)](#83-queue-implementation-array-based)
    - [8.4. Real-World Uses](#84-real-world-uses)
  - [9. Linked Lists](#9-linked-lists)
    - [9.1. What is a Linked List?](#91-what-is-a-linked-list)
    - [9.2. Node Structure](#92-node-structure)
    - [9.3. Linked List vs Array](#93-linked-list-vs-array)
    - [9.4. Key Insight](#94-key-insight)
    - [9.5. Linked List Implementation](#95-linked-list-implementation)
    - [9.6. Queue with Linked List (O(1) Operations)](#96-queue-with-linked-list-o1-operations)
  - [10. Binary Trees](#10-binary-trees)
    - [10.1. What is a Binary Tree?](#101-what-is-a-binary-tree)
    - [10.2. Binary Tree Properties](#102-binary-tree-properties)
    - [10.3. Binary Tree Operations](#103-binary-tree-operations)
    - [10.4. BST Implementation](#104-bst-implementation)
    - [10.5. Why Binary Trees are Fast](#105-why-binary-trees-are-fast)
    - [10.6. BST Traversals (Return List of Values)](#106-bst-traversals-return-list-of-values)
    - [10.7. BST exists(val)](#107-bst-existsval)
    - [10.8. BST Quiz](#108-bst-quiz)
    - [10.9. Problem: Unbalanced Trees](#109-problem-unbalanced-trees)
    - [10.10. Tree Traversal](#1010-tree-traversal)
  - [11. Red-Black Trees](#11-red-black-trees)
    - [11.1. The Problem with Binary Trees](#111-the-problem-with-binary-trees)
    - [11.2. Red-Black Tree Rules](#112-red-black-tree-rules)
    - [11.3. Rotations](#113-rotations)
    - [11.4. Fix-Up Process](#114-fix-up-process)
  - [12. Hashmaps](#12-hashmaps)
    - [12.1. What is a Hashmap?](#121-what-is-a-hashmap)
    - [12.2. How Hashmaps Work](#122-how-hashmaps-work)
    - [12.3. Hash Function Requirements](#123-hash-function-requirements)
    - [12.4. Simple Hashmap Implementation (Toy)](#124-simple-hashmap-implementation-toy)
    - [12.5. Hashmap Operations](#125-hashmap-operations)
    - [12.6. Limitations of Simple Hashmap](#126-limitations-of-simple-hashmap)
    - [12.7. Production Hashmaps](#127-production-hashmaps)
    - [12.8. Real-World Use](#128-real-world-use)
  - [13. Tries](#13-tries)
    - [13.1. What is a Trie?](#131-what-is-a-trie)
    - [13.2. Trie Structure](#132-trie-structure)
    - [13.3. Trie Implementation](#133-trie-implementation)
    - [13.4. find\_matches(document)](#134-find_matchesdocument)
    - [13.5. Trie Operations](#135-trie-operations)
    - [13.6. Real-World Uses](#136-real-world-uses)
  - [14. Graphs](#14-graphs)
    - [14.1. What is a Graph?](#141-what-is-a-graph)
    - [14.2. Graph Representations](#142-graph-representations)
    - [14.3. Graph Implementation (Adjacency Matrix)](#143-graph-implementation-adjacency-matrix)
    - [14.4. Graph Quiz](#144-graph-quiz)
    - [14.5. Graph Implementation (Adjacency List)](#145-graph-implementation-adjacency-list)
    - [14.6. Real-World Uses](#146-real-world-uses)
    - [14.7. Complete Graph](#147-complete-graph)
  - [15. Breadth-First Search (BFS)](#15-breadth-first-search-bfs)
    - [15.1. What is BFS?](#151-what-is-bfs)
    - [15.2. BFS Algorithm](#152-bfs-algorithm)
    - [15.3. BFS Implementation](#153-bfs-implementation)
    - [15.4. BFS Complexity](#154-bfs-complexity)
    - [15.5. When to Use BFS](#155-when-to-use-bfs)
    - [15.6. BFS Disadvantages](#156-bfs-disadvantages)
  - [16. Depth-First Search (DFS)](#16-depth-first-search-dfs)
    - [16.1. What is DFS?](#161-what-is-dfs)
    - [16.2. DFS Algorithm (Recursive)](#162-dfs-algorithm-recursive)
    - [16.3. DFS Implementation](#163-dfs-implementation)
    - [16.4. DFS Complexity](#164-dfs-complexity)
    - [16.5. When to Use DFS](#165-when-to-use-dfs)
    - [16.6. DFS Disadvantages](#166-dfs-disadvantages)
  - [17. P vs NP](#17-p-vs-np)
    - [17.1. Complexity Classes](#171-complexity-classes)
    - [17.2. Key Insight](#172-key-insight)
    - [17.3. The P vs NP Question](#173-the-p-vs-np-question)
    - [17.4. Why It Matters](#174-why-it-matters)
    - [17.5. NP-Complete Problems](#175-np-complete-problems)
    - [17.6. Password Guessing (get\_num\_guesses)](#176-password-guessing-get_num_guesses)
    - [17.7. NP-Hard vs NP-Complete](#177-np-hard-vs-np-complete)
    - [17.8. Real-World Example: Password Verification](#178-real-world-example-password-verification)
  - [18. Prime Factorization](#18-prime-factorization)
    - [18.1. The Problem](#181-the-problem)
    - [18.2. Factorization Algorithm](#182-factorization-algorithm)
    - [18.3. Complexity Analysis](#183-complexity-analysis)
    - [18.4. Cryptography Implication](#184-cryptography-implication)
    - [18.5. P vs NP Implication](#185-p-vs-np-implication)
  - [19. Summary](#19-summary)
    - [19.1. Key Takeaways](#191-key-takeaways)
    - [19.2. Complexity Classes Quick Reference](#192-complexity-classes-quick-reference)
    - [19.3. Further Learning](#193-further-learning)


---

## 0. Introduction

### 0.1. Why Learn Data Structures and Algorithms?

Even if you never write a heap or quicksort algorithm from scratch in your career, understanding DSA is critical for two main reasons:

1. **Understand Performance Implications**: You need to understand how your code performs at scale. Users always want fast applications.

2. **Practice Solving Hard Problems**: The specific problems you solve day-to-day won't be these exact problems or algorithms, but they will be hard. Learning DSA fundamentals prepares you to tackle difficult problems when they come.

### 0.2. Course Topics Covered

- Introduction to algorithms
- Math for programmers
- Big O analysis
- Sorting algorithms
- Exponential time
- Introduction to data structures
- Stacks
- Queues
- Linked lists
- Binary trees
- Red-black trees
- Hashmaps
- Tries
- Graphs
- Depth-first and breadth-first search
- P versus NP

---

## 1. Introduction to Algorithms

### 1.1. What is an Algorithm?

An algorithm is a finite sequence of well-defined, computer-implementable instructions used to solve a problem.

**Key Characteristics:**
1. **Defined**: There must be a specific sequence of steps
2. **Unambiguous**: Cannot be up to interpretation - either correct or incorrect
3. **Implementable**: Must be possible to carry out in hardware or software

### 1.2. Three Goals of This Course

1. **Think Algorithmically**: Develop algorithmic thinking patterns
2. **Learn Performance Optimization**: Understand how algorithms affect performance
3. **Practice Solving Hard Problems**: Build problem-solving skills

### 1.3. Important Philosophy

**Don't memorize algorithms** - instead, focus on understanding how they work. It's a waste of time to memorize anything that's a Google search away unless you're cramming for an interview.

### 1.4. Example: Find Minimum Algorithm

**Problem**: Find the minimum value in a list of numbers.

**Algorithm Steps**:
1. Set minimum to positive infinity
2. Loop through each number in the list
3. If the current number is less than minimum, update minimum
4. Return minimum

**Code Example**:
```python
def find_minimum(nums):
    '''
    Docstring for find_minimum
    
    :param nums: Find the minimum value in a list of numbers.
    '''
    if len(nums) == 0: # to handle cases containing nothing : []
        return None
    
    min_val = float('inf') # comparing wit biggest value, infinity
    
    for num in nums:
        if num < min_val:
            min_val = num
    
    return min_val
```

**Edge Case**: Handle empty lists by returning `None`. If you return positive infinity for an empty list, tests expect `None`.

**Tip**: Check the test code if unsure what to expect for edge cases.

### 1.5. Algorithm Must Be Finite

An algorithm must have a **finite** number of steps (not unbounded, uncountable, or infinite).

### 1.6. Pseudocode: Mystery Algorithm (Reverse String)

- Start with original string `S` and empty string `R`.
- Loop through `S` from last character to first.
- For each character, add it to the end of `R`.
- Result: `R` is the reverse of `S` (e.g. "dog" → "god").
- It does **not** generate a palindrome, download a virus, or double the string length.

### 1.7. Simple Algorithms Example: Sum

**Problem**: Sum all numbers in a list.

```python
def sum_numbers(nums):
    if len(nums) == 0:
        return 0

    s = 0
    for n in nums:
        s+=n
    return s

l1 = [1,23,45,566]
print(sum_numbers(l1))
# 635
```

**Edge Case**: Empty list should return 0

### 1.8. Simple Algorithms Example: Find Longest String

```py
def find_longest_string(lst):
    longest_so_far= ""
    for s in lst:
        if len(s) > len(longest_so_far):
            longest_so_far = s
    return longest_so_far

list_of_words = ["Bali","Bhati", "Bhaskar"]

print(find_longest_string(list_of_words))
# Bhaskar
```

---

## 2. Math for Programmers

### 2.1. Exponents

An exponent indicates how many times a number is multiplied by itself.

**Examples**:
- 5³ = 5 × 5 × 5 = 125
- 2⁴ = 2 × 2 × 2 × 2 = 16
- 3⁵ = 3 × 3 × 3 × 3 × 3 = 243

**In Python**: Use double asterisk `**`
```python
square = 2 ** 2  # 4
cube = 2 ** 3    # 8
```

**Special Cases**:
- Anything raised to the power of 1 equals itself: 5¹ = 5
- Anything raised to the power of 0 equals 1: 5⁰ = 1

**Key Insight**: Results of exponentiation grow VERY quickly.

**Powers of 2**: 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 (2^10 = 1024).

**Powers of 10**: 10^1 = 10, 10^2 = 100, 10^3 = 1000 — exponent is the number of zeros.

### 2.2. Exercise: Get Estimated Spread (Social Litics)

**Formula**: `estimated_spread = average_audience_followers × (num_followers)^1.2`

- `audience_followers`: list of follower counts of the author's followers.
- Average = sum of list / length. If list is empty, return 0.
- In Python: `return (sum / num_followers) * (num_followers ** 1.2)`.

### 2.3. Geometric Sequences

A geometric sequence is where each number is calculated by multiplying the previous number by a fixed number (the common ratio r).

**Formula**: a_n = a₁ × r^(n-1)

**Example**: Starting with 100, if r = 3:
- First: 100
- Second: 100 × 3 = 300
- Third: 300 × 3 = 900
- Seventh: 100 × 3⁶ = 72,900

### 2.4. Exercise: Get Follower Prediction (Geometric Growth)

- **Fitness** influencers: follower count **quadruples** each month (factor = 4).
- **Cosmetic** influencers: follower count **triples** each month (factor = 3).
- **All other** types: follower count **doubles** each month (factor = 2).
- Return: `follower_count * (factor ** num_months)`.
- Use a match/case or if/elif to set `factor` from `influencer_type`.

### 2.5. Nonlinear Growth

Exponents are important for understanding algorithm execution speed. Results from multiplication, exponentiation, and other operations:
- **Linear (2x)**: Slowest growth
- **Multiplication**: Medium growth
- **Exponentiation**: Fastest growth

**Quiz**: Which operation's result grows fastest? — **Exponentiation**.

**Quiz**: How much larger is 2^64 than 2^32? — **2^32 times larger** (because 2^32 × 2^32 = 2^64).

### 2.6. Logarithms

A logarithm is the inverse operation of exponentiation.

**Definition**: log_b(x) = y means b^y = x

**Examples**:
- log₂(8) = 3 (because 2³ = 8)
- log₂(16) = 4 (because 2⁴ = 16)
- log₂(32) = 5 (because 2⁵ = 32)
- log₁₀(1,000) = 3 (because 10³ = 1,000)

**Key Insight**: Logarithms grow VERY slowly compared to exponents.

**Why They Matter**: 
- Exponents grow very quickly
- Logarithms grow very slowly
- In programming, logarithmic algorithms are highly desirable
- Binary search is O(log n) - even with 1 million items, only 20 comparisons needed

**In Python**:
```python
import math
result = math.log(value, base)  # log base 'base' of value
# e.g. math.log(num_followers, 2) for log base 2
```

**Quiz**: log base 3 of 9 = ? — **2** (3×3=9).
**Quiz**: Is log base 5 of 5 greater than 5^5? — **False** (log_5(5)=1; 5^5 is much larger).
**Quiz**: Result of which operation grows slowest? — **Logarithm**.

**Exercise: Get Influencer Score** — `average_engagement_percentage * math.log(num_followers, 2)`.

### 2.7. Factorials

The factorial of a positive integer n (written as n!) is the product of all positive integers less than or equal to n.

**Examples**:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 3! = 3 × 2 × 1 = 6

**Key Insight**: Factorials grow even faster than exponents.

**Usage**: Factorials are useful for counting permutations (how many ways a collection can be ordered).

**Quiz**: How much larger is 564! than 563!? — **564 times** (564! = 563! × 564).
**Quiz**: Which grows fastest as n increases: n², n!, n, log₂(n)? — **n!**.

**Exercise: Num Possible Orders** — Number of ways to order `num_posts` posts = factorial. Use a product starting at 1: `for i in range(1, num_posts + 1): p *= i`.

---

## 3. Big O Analysis

### 3.1. What is Big O?

Big O notation is a way to categorize algorithms by how they slow down as input size grows. We're specifically worried about the **worst-case runtime**.

**Key Principle**: Big O only cares about how the algorithm scales, not the actual time in nanoseconds.

### 3.2. Constant Time: O(1)

Operations that take the same time regardless of input size.

**Examples**:
- Array indexing: `arr[5]` is always fast
- Dictionary lookup: `dict['key']` is always fast
- Returning a property

```python
def get_first_element(arr):
    return arr[0]  # O(1) - always takes same time
```

### 3.3. Linear Time: O(n)

Time grows proportionally with input size.

**Examples**:
- Looping through an entire array once
- Finding an item via linear search

```python
def find_item(arr, target):
    for item in arr:
        if item == target:
            return True
    return False  # O(n)
```

### 3.4. Logarithmic Time: O(log n)

Time grows logarithmically - only a few more steps for much larger input.

**Example**: Binary search
- 4 items → 2 comparisons
- 8 items → 3 comparisons  
- 16 items → 4 comparisons
- 1 million items → ~20 comparisons

```python
# Example: How many times can we divide by 2?
def count_divisions(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count  # O(log n)
```

### 3.5. Linearithmic Time: O(n log n)

Combination of linear and logarithmic - the "sweet spot" for many sorting algorithms.

**Examples**: Merge sort, quicksort (average case)

### 3.6. Quadratic Time: O(n²)

Time grows with the square of input size - common with nested loops.

**Examples**: Bubble sort, nested iterations

```python
def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # O(n²)
```

**Note**: Generally try to avoid O(n²) algorithms for large datasets.

### 3.7. Two Variables: O(n·m)

When you have two different input sizes that matter.

```python
def get_average_brand_followers(all_handles, brand_name):
    count = 0
    for handles_list in all_handles:
        for handle in handles_list:
            if brand_name in handle:
                count += 1
    
    average = count / len(all_handles)
    return average  # O(n·m) where n = number of lists, m = average list length
```

### 3.8. Exponential Time: O(2^n)

Time grows exponentially - practically impossible for even moderate input sizes.

- 15 items: ~32,000 iterations
- 20 items: ~1,000,000 iterations
- 30 items: ~1,000,000,000+ iterations

**Example**: Generating power sets (all subsets)

### 3.9. Factorial Time: O(n!)

Even worse than exponential - almost never practical.

**Example**: Finding all permutations

```python
# Generating all permutations is O(n!)
from itertools import permutations
for perm in permutations(items):
    process(perm)
```

### 3.10. Big O Complexity Chart (Best to Worst)

1. O(1) - Constant
2. O(log n) - Logarithmic
3. O(n) - Linear
4. O(n log n) - Linearithmic
5. O(n²) - Quadratic
6. O(n³) - Cubic
7. O(2^n) - Exponential
8. O(n!) - Factorial

### 3.11. Important: Constants Don't Matter

O(2n) simplifies to O(n) - constants are ignored.

**Examples**:
- O(2×n) = O(n)
- O(5) = O(1)
- O(2×log n) = O(log n)
- **Exception**: O(2^n) cannot be simplified (can't remove the 2)

**Quiz**: Which algorithm tends to run slowest? n², n, log n, constant — **n²**.
**Quiz**: Reduce O(2×log(2×n)) — drop constants → **O(log n)**.
**Quiz**: Sum vs double_sum — both O(n); which takes longer in practice? **double_sum** (does more work per element).
**Quiz**: get_name_at_index(names, i) → return names[i] — **O(1)** (index lookup).
**Quiz**: Loop that divides n by 2 until n ≤ 1 — **O(log n)** (number of steps grows logarithmically with n).

### 3.12. Find Max (O(n))

Same idea as find min: initialize `max_val = float('-inf')`, loop and update if `num > max_val`, return max. No iteration = O(n).

### 3.13. Find Full Name (O(n²))

Given `first_names`, `last_names`, and a `full_name` string: nested loop over first and last; if `f"{first} {last}" == full_name` return True; else False. Worst case is last pair → O(n²).

### 3.14. Average Brand Followers (O(n·m))

`all_handles`: list of lists of strings (handles per influencer). Count how many handles contain `brand_name` (e.g. "Cosmo"), then return count / len(all_handles). Use `if brand_name in handle` for each handle.

### 3.15. Find Last Name (O(1))

Given `names_dict` (first_name → last_name) and `first_name`: use **dictionary lookup** instead of looping. `return names_dict.get(first_name)` — O(1). Using a loop would be O(n) and too slow for large data.

### 3.16. Binary Search (O(log n)) — Full Steps

- **Input**: Sorted array, target.
- **Invariants**: `low = 0`, `high = len(arr) - 1`.
- **Loop**: `while low <= high`:
  - `median = (low + high) // 2`
  - If `arr[median] == target` → return True
  - If `arr[median] < target` → `low = median + 1`
  - Else → `high = median - 1`
- Return False if loop exits. Each step halves the search space → O(log n).

---

## 4. Sorting Algorithms

### 4.1. Built-in Sorting (Python)

Use `sorted(list)` or `list.sort()`. For custom order, use `key`: e.g. `sorted(influencers, key=vanity)`.

### 4.2. Exercise: Vanity Sort (Social Litics)

- **vanity(influencer)**: `influencer.num_bio_links * 5 + influencer.num_selfies` (links weighted more).
- **vanity_sort(influencers)**: `return sorted(influencers, key=vanity)` (least to greatest by vanity score).

### 4.3. Why Learn Sorting?

Even though languages provide built-in sorting (like Python's `sorted()`), understanding sorting algorithms teaches valuable lessons about:
- Algorithm design
- Performance tradeoffs
- When to use which algorithm

### 4.4. Bubble Sort

**How it works**:
1. Loop through the array
2. Compare adjacent pairs
3. Swap if out of order
4. Repeat until no swaps occur

**Characteristics**:
- **Big O**: O(n²)
- **Best case**: O(n) if already sorted (no swaps needed)
- **Space**: Sorts in place (O(1) extra space)
- **Stable**: Maintains order of equal elements
- **Real-world use**: Almost never - too slow

```python
def bubble_sort(nums):
    end = len(nums)
    swapping = True
    
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                # Swap
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
        
        end -= 1
    
    return nums
```

### 4.5. Merge Sort

**How it works** (Divide and Conquer):
1. Divide array into halves recursively until single elements
2. Merge sorted halves back together in order

**Characteristics**:
- **Big O**: O(n log n) always
- **Space**: Requires extra space for copies
- **Stable**: Yes
- **Real-world use**: Very common, reliable

```python
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

**Why Merge Sort?**
- Guaranteed O(n log n)
- Stable sort
- Good for large datasets

### 4.6. Insertion Sort

**How it works**:
1. Start at second element
2. Compare with elements to the left
3. Insert into correct position
4. Repeat for each element

**Characteristics**:
- **Big O**: O(n²) average/worst, O(n) best case (pre-sorted)
- **Space**: Sorts in place
- **Stable**: Yes
- **Real-world use**: Small datasets, mostly-sorted data

```python
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    
    return nums
```

**Why Insertion Sort?**
- Fast on small lists
- No memory overhead
- Adaptive (fast on nearly-sorted data)
- Many production libraries use it for small subarrays

### 4.7. Quicksort

**How it works** (Divide and Conquer):
1. Choose a pivot element
2. Partition: put smaller elements left, larger right
3. Recursively sort both sides

**Characteristics**:
- **Big O**: O(n log n) average, O(n²) worst case
- **Space**: O(log n) for recursion
- **Stable**: Typically no
- **Real-world use**: Very common (default in many languages)

```python
def quicksort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quicksort(nums, low, pivot_index - 1)
        quicksort(nums, pivot_index + 1, high)
    
    return nums

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    
    nums[i], nums[high] = nums[high], nums[i]
    return i
```

**Avoiding O(n²) Worst Case**:
- Shuffle input randomly
- Use median-of-three pivot selection
- Both ensure O(n log n) average case

**Why Quicksort?**
- Fast on average
- Sorts in place
- Cache-friendly
- Widely used in production

### 4.8. Sorting Quiz Summary

- **Bubble sort best case**: O(n) when data is pre-sorted (no swaps). **Worst**: O(n²).
- **Good reason to use bubble sort**: You're studying algorithms (not for speed or memory).
- **Merge sort**: Recursive (calls itself); **O(n log n)**; stable; uses extra memory.
- **Insertion sort**: O(n²) average; O(n) best when pre-sorted; **least memory**; good for **very small** inputs; some production sort implementations use it for small subarrays.
- **Quicksort worst case**: **Already sorted** input (pivot is min/max each time) → O(n²). Fix: **shuffle input** (practically ensures O(n log n)) or **median-of-three** pivot (no randomness, deterministic).
- **Stable sort** (preserves order of equal keys): **Merge sort** (quicksort typically not).
- **More likely in production**: **Quicksort** (e.g. default in many languages; Postgres uses it).

---

## 5. Exponential Time

### 5.1. Polynomial vs Exponential

**Polynomial Time Algorithms**: Run in acceptable time for practical use.
- Examples: O(n), O(n log n), O(n²), O(n³)

**Exponential Time Algorithms**: Become impractical very quickly.
- Examples: O(2^n), O(n!)
- Even small inputs become impossible

### 5.2. Fibonacci Sequence

**Problem**: Calculate the nth Fibonacci number where each number is the sum of the two before it.

**Naive Recursive Solution** (Exponential Time):
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # O(2^n) - recalculates same values
```

**Optimized Solution** (Polynomial Time):
```python
def fib(n):
    if n <= 1:
        return n
    
    grandparent = 0
    parent = 1
    
    for i in range(1, n):
        current = parent + grandparent
        grandparent = parent
        parent = current
    
    return current  # O(n) - much faster!
```

**Key Insight**: Convert recursion to iteration to avoid recalculating values.

### 5.3. Power Set

**Problem**: Generate all subsets of a set (power set).

**Example**: Power set of {1, 2, 3} is {{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}

```python
def power_set(items):
    if len(items) == 0:
        return [[]]
    
    first = items[0]
    remaining = power_set(items[1:])
    
    result = []
    for subset in remaining:
        result.append(subset)
        result.append([first] + subset)
    
    return result
```

**Characteristics**:
- **Big O**: O(2^n) - output itself has 2^n elements
- **Practical limits**: 25 items ≈ 9 hours, 40 items ≈ 34 years
- **Not practical** for large inputs

### 5.4. Chapter 5 Quiz

- **Polynomial vs exponential**: Polynomial algorithms are **faster** than exponential.
- **Algorithms in P**: **More practical** to solve with computers.
- **Fibonacci (reduction to P)**: Replace recursion with loop; keep `grandparent`, `parent`, `current`; update in loop: `current = parent + grandparent`, then shift (grandparent=parent, parent=current). Return current after loop. O(n).
- **Power set**: Base case `if len(items)==0: return [[]]`. Recursive: `first = items[0]`, `remaining = power_set(items[1:])`. Build result: for each subset in remaining, append subset and append `[first]+subset`. Return result.
- **Big O review**: Which tends to be fastest? **O(n)** among the options given (vs n², n log n, 2^n).
- **get_name_at_index**: Direct index → **O(1)**.
- **Loop dividing by 2 until ≤1**: **O(log n)**.
- **Tricky loop** (inner loop size shrinks: n, n/2, n/4, ...): Forms geometric series → **O(n)** when fully reduced. Equivalent but not fully reduced: O(n/2 + n/4 + ...).

---

## 6. Introduction to Data Structures

### 6.1. What are Data Structures?

A data structure:
1. **Stores data** - holds data values
2. **Organizes data** - arranges for efficient access/modification
3. **Provides operations** - exposes functions to read/write data

**Key relationship**: Data structures use algorithms, and algorithms use data structures.

### 6.2. Exercise: Count Markers (Locked In)

- **Input**: List of strings `job_titles`.
- **Output**: Number of users whose title is the string `"marketer"`.
- **Edge**: Locked-in users may use different casing — compare with `job_title.lower() == "marketer"`.
- **Implementation**: count = 0; for each title, if match then count += 1; return count.

### 6.3. Exercise: Last Work Experience

- **Input**: List of work history strings (oldest to most recent).
- **Output**: Last place they worked (most recent). If empty, return `None`.
- **Implementation**: `if len(work_experiences) == 0: return None`; `return work_experiences[-1]` (or `work_experiences[len(work_experiences)-1]`).
- **Big O**: **O(1)** — length is stored, indexing is O(1). No iteration.
- **Why index lookup is fast**: The computer jumps straight to the memory location; the index is like an address. No scanning.

### 6.4. Lists (Arrays)

**Built-in Data Structure** in Python.

**Operations**:
- **Append**: O(1) - add to end
- **Index**: O(1) - access by position
- **Delete from middle**: O(n) - must shift elements (everything after shifts down)
- **Search**: O(n) - must check each element (values are not ordered by value; list is ordered by index only)

**Lists struggle when**: Frequently deleting from the middle or frequently searching for a specific value.

**Quiz**: Data structures store data and allow efficient access. Which is **not** a data structure? **MySQL** (it's a database). Arrays, dictionaries, and tuples are in-memory data structures.

### 6.5. Tuples

**Immutable** version of lists - cannot be modified after creation.

---

## 7. Stacks

### 7.1. What is a Stack?

A stack is a Last-In-First-Out (LIFO) data structure:
- Items added to the **top**
- Items removed from the **top**
- Like a stack of plates - you take from the top, add to the top

### 7.2. Stack Operations

All operations are **O(1) constant time**:

1. **Push**: Add item to top
2. **Pop**: Remove and return item from top
3. **Peek**: View top item without removing
4. **Size**: Get number of items

### 7.3. Stack Implementation

- **Top of stack** = end of list (so push = append, pop/peek = last element).
- **Push**: `self.items.append(item)`.
- **Size**: `return len(self.items)`.
- **Peek**: If empty return None; else `return self.items[-1]`.
- **Pop**: If empty return None; else save `val = self.items[-1]`, `del self.items[-1]`, return val. (Can use tuple swap instead of del.)

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item
    
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
```

**Quiz**: Which operations are O(1)? **All of them** (size, push, pop, peek).
**Quiz**: Where can items be added/removed? **Top only**.
**Quiz**: What can be stored? **Anything** (objects, integers, etc.).
**Quiz**: Big O to retrieve item at **bottom** of stack? **O(n)** — must pop all items above it first (stack doesn't support direct access).

### 7.4. Real-World Uses

1. **Undo/Redo**: Each action pushed onto stack
2. **Browser Back Button**: Navigation history
3. **Function Call Stack**: How programs track function calls
4. **Expression Evaluation**: Evaluating mathematical expressions

### 7.5. Example: Balanced Parentheses

**Problem**: Check if parentheses in a string are balanced. Only consider '(' and ')'.

**Algorithm**: On '(', push onto stack (push a **non-None** value, e.g. `True` or `'('`, so that "empty stack" means balanced). On ')', pop; if pop returns None (stack was empty) → **unbalanced** (too many closing) → return False. After loop, return True if stack is empty (e.g. `stack.peek() is None`), else False.

**Bug to avoid**: Do not push `None` for '(' — then at the end `peek() is None` would indicate "empty" but you'd have pushed None, so the test would be wrong. Push any non-None value.

```python
def is_balanced(s):
    stack = Stack()
    for char in s:
        if char == '(':
            stack.push(True)  # or stack.push('(') — not None
        elif char == ')':
            if stack.pop() is None:
                return False
    return stack.peek() is None
```

---

## 8. Queues

### 8.1. What is a Queue?

A queue is a First-In-First-Out (FIFO) data structure:
- Items enter at the **back** (enqueue)
- Items leave at the **front** (dequeue)
- Like a line at a coffee shop

### 8.2. Queue Operations

All operations are **O(1) constant time** (with proper implementation):

1. **Enqueue (Push)**: Add to back
2. **Dequeue (Pop)**: Remove from front
3. **Peek**: View front item
4. **Size**: Get number of items

### 8.3. Queue Implementation (Array-Based)

- **Tail** = where items enter (e.g. index 0): `self.items.insert(0, item)`.
- **Head** = where items leave (e.g. last index): pop from end, peek at end.
- **Push**: `self.items.insert(0, item)` — O(n) because all elements shift.
- **Pop**: if empty return None; else `item = self.items[-1]`, remove last (e.g. `del self.items[-1]` or slice), return item.
- **Peek**: if empty return None; else return `self.items[-1]`.
- **Size**: `return len(self.items)`.

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item
    
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
```

**Problem**: This implementation has O(n) push because inserting at index 0 requires shifting all elements.

**Quiz**: Big O of push, pop, peek, size in an **optimized** queue? **All O(1)**.
**Quiz**: If an item could be anywhere in the queue, big O to retrieve it? **O(n)** (may need to dequeue everything).
**Quiz**: Why is our list-based queue's push O(n)? **Because we have to move all elements over by one index** to make room at the front.

### 8.4. Real-World Uses

1. **Job Scheduling**: Process jobs in order received
2. **BFS Algorithms**: Breadth-first search traversal
3. **Printer Queues**: Documents print in order received
4. **Networking**: Message queues, packet processing

---

## 9. Linked Lists

### 9.1. What is a Linked List?

A linked list is a data structure where:
- Each element (node) contains a value and a reference to the next node
- Nodes can be scattered in memory (unlike arrays)
- Perfect for building efficient queues

### 9.2. Node Structure

- **Constructor**: `self.val = value`, `self.next = None`.
- **set_next(node)**: `self.next = node`.
- Nodes live in non-consecutive memory; each node holds value and reference to next. End of list: `next` is None.

```python
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
    
    def set_next(self, node):
        self.next = node
```

### 9.3. Linked List vs Array

**Arrays** (Consecutive Memory):
- Fast index access: O(1)
- Slow middle insertion/deletion: O(n)
- Must shift all elements after insertion point

**Linked Lists** (Scattered Memory):
- Slow index access: O(n)
- Fast middle insertion/deletion: O(1)
- Only update two pointers

### 9.4. Key Insight

Linked lists avoid memory shifting when inserting/deleting at the beginning, making them perfect for queue implementations.

### 9.5. Linked List Implementation

- **Constructor**: `self.head = None`, `self.tail = None` (tail for O(1) add_to_tail).
- **__iter__**: Generator that **yields each node** (not node.val): `temp = self.head`, `while temp: yield temp`, `temp = temp.next`. This allows `for node in self:` and uses `yield`.
- **add_to_tail(node)**: If `self.head is None`: set `self.head = self.tail = node`. Else: `self.tail.next = node`, `self.tail = node`. With tail reference this is O(1).
- **add_to_head(node)**: `node.next = self.head`, `self.head = node`. If list was empty (`self.head` was None before), set `self.tail = node`.
- **remove_from_head()**: If `self.head is None` return None. `temp = self.head`, `self.head = self.head.next`. If `self.head is None` then `self.tail = None`. Set `temp.next = None` (cleanup), return temp.

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def add_to_head(self, node):
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
    
    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        temp.next = None
        return temp
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
```

**Quiz**: Find an item in a linked list — **iterate through all nodes by following next references** (no indexing, no "sending thoughts and prayers").
**Quiz**: Linked lists have faster time complexity than regular lists for — **inserting/deleting items in the middle** (not for iterating, appending, or index access).
**Quiz**: Queue made with linked list instead of array — **can have O(1) push and pop** (linked list uses more memory, is not simpler, and is not faster to search).

### 9.6. Queue with Linked List (O(1) Operations)

```python
class LinkedListQueue:
    def __init__(self):
        self.items = LinkedList()
    
    def push(self, item):  # O(1)
        self.items.add_to_tail(item)
    
    def pop(self):  # O(1)
        return self.items.remove_from_head()
```

**Why This Works**: Both operations only update tail/head pointers - no element shifting needed!

---

## 10. Binary Trees

### 10.1. What is a Binary Tree?

A binary tree is a data structure where:
- Each node has at most **2 children** (left and right)
- All values to the **left** are smaller
- All values to the **right** are larger
- Called a Binary Search Tree (BST)

### 10.2. Binary Tree Properties

**Key Rule**: For any node with value X:
- All left descendants have values < X
- All right descendants have values > X
- No duplicates

**Quiz**: Nodes in a binary tree can have at most **two** child nodes. Binary search trees must be **ordered** (left < parent < right). Parent nodes can have **many** children; children can have **one** parent (in trees).

### 10.3. Binary Tree Operations

All operations are **O(log n)** on average (balanced tree):

1. **Insert**: O(log n) - find spot, add node
2. **Search**: O(log n) - eliminate half tree with each comparison
3. **Delete**: O(log n) - find node, restructure
4. **Min/Max**: O(log n) - traverse to leftmost/rightmost

### 10.4. BST Implementation

```python
class BSTNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        
        if self.val == val:
            return  # No duplicates
        
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
    
    def search(self, val):
        if self.val == val:
            return True
        
        if val < self.val and self.left:
            return self.left.search(val)
        elif val > self.val and self.right:
            return self.right.search(val)
        
        return False
    
    def get_min(self):
        current = self
        while current.left:
            current = current.left
        return current.val
    
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.val
    
    def delete(self, val):
        if self.val is None:
            return None
        
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        
        # Found node to delete
        if not self.left:
            return self.right
        if not self.right:
            return self.left
        
        # Has both children: find min in right subtree (leftmost of right), copy value, delete that node
        min_larger = self.right.get_min()
        self.val = min_larger
        self.right = self.right.delete(min_larger)
        
        return self
```

### 10.5. Why Binary Trees are Fast

For a balanced tree with n nodes:
- Depth = log₂(n)
- Each comparison eliminates half the tree
- 1 million items = only ~20 levels deep

**Example Depths**:
- 8 nodes → 3 levels
- 16 nodes → 4 levels
- 1 million nodes → ~20 levels

### 10.6. BST Traversals (Return List of Values)

- **Pre-order**: current, then left, then right. `visited.append(self.val)` then recurse left (if self.left), then right (if self.right). Return visited.
- **Post-order**: left, then right, then current. Recurse left, recurse right, then append self.val.
- **In-order**: left, then current, then right. Recurse left, append self.val, recurse right. Produces sorted order.

Guard: only recurse if `self.left` / `self.right` is not None.

### 10.7. BST exists(val)

If `self.val == val` return True. If `val < self.val` and `self.left`: return `self.left.exists(val)`. If `val > self.val` and `self.right`: return `self.right.exists(val)`. Else return False. O(log n) average.

### 10.8. BST Quiz

- **If 100 sorted items inserted in order**, BST becomes a single branch (linked list) → lookups **O(n)**.
- **Assuming tree stays balanced**, will operations ever degrade past O(log n)? **No**.
- **Approximate depth of tree with 16,000 nodes**: log₂(16000) ≈ **14** (e.g. 2^14 = 16384).
- **Average big O of insert and delete**: **O(log n)**.

### 10.9. Problem: Unbalanced Trees

If you insert sorted data, tree degrades to a linked list:

```
Insert 1,2,3,4,5:
    1
     \
      2
       \
        3
         \
          4
```

This becomes O(n) instead of O(log n)!

### 10.10. Tree Traversal

**Pre-Order** (Visit node before children): 4, 2, 1, 3, 7, 6, 8

```python
def preorder(node, visited):
    if node is None:
        return visited
    visited.append(node.val)
    preorder(node.left, visited)
    preorder(node.right, visited)
    return visited
```

**Post-Order** (Visit node after children): 1, 3, 2, 6, 8, 7, 4

```python
def postorder(node, visited):
    if node is None:
        return visited
    postorder(node.left, visited)
    postorder(node.right, visited)
    visited.append(node.val)
    return visited
```

**In-Order** (Visits in sorted order): 1, 2, 3, 4, 6, 7, 8

```python
def inorder(node, visited):
    if node is None:
        return visited
    inorder(node.left, visited)
    visited.append(node.val)
    inorder(node.right, visited)
    return visited
```

---

## 11. Red-Black Trees

### 11.1. The Problem with Binary Trees

Unbalanced trees can degrade to O(n) performance. Red-black trees maintain balance automatically.

### 11.2. Red-Black Tree Rules

Every node is either **red** or **black**:

1. Each node is red or black
2. The root is black
3. All leaf nodes (nil) are black
4. If a node is red, both children are black
5. All paths from a node to descendants have the same number of black nodes

**Result**: Maximum depth = 2 × log₂(n), so O(log n) guaranteed!

### 11.3. Rotations

When rules are violated, rotations rebalance the tree:

**Left Rotation**: Move right child up, parent becomes left child
```python
def rotate_left(pivot_parent):
    pivot = pivot_parent.right
    pivot_parent.right = pivot.left
    
    if pivot.left:
        pivot.left.parent = pivot_parent
    
    pivot.parent = pivot_parent.parent
    
    if pivot_parent == self.root:
        self.root = pivot
    elif pivot_parent.parent.left == pivot_parent:
        pivot_parent.parent.left = pivot
    else:
        pivot_parent.parent.right = pivot
    
    pivot.left = pivot_parent
    pivot_parent.parent = pivot
```

**Right Rotation**: Mirror of left rotation

### 11.4. Fix-Up Process

After insertion, violations are fixed by:
1. Recoloring nodes (red ↔ black)
2. Performing rotations when needed

This maintains balance automatically, keeping all operations O(log n).

**Red-Black Notes**: Red-black trees are **not** perfectly balanced but are balanced enough for O(log n). Insert: add node as in BST, color it red, set left/right to nil, then call fix_insert. fix_insert: while new_node != root and parent is red, get grandparent; if parent is grandparent's right: uncle = grandparent.left; if uncle red then recolor and move up; else if new_node is parent's left then rotate right and recolor; else symmetric for parent left. Finally set root to black.

**Quiz**: Is a tree where a red node has a red child valid? **No** — breaks rule 4 (red node must have black children).
**Quiz**: To be valid, must a black node have red children? **No** — black nodes can have black children.
**Quiz**: Red-black trees perfectly balanced? **No**. They always have worst-case O(log n) insertion, lookup, deletion? **Yes**.

---

## 12. Hashmaps

### 12.1. What is a Hashmap?

A hashmap (dictionary in Python) is a key-value data structure that provides **O(1)** lookup.

**Built-in Hashmap**: Python's dictionary uses hashmaps under the hood.

### 12.2. How Hashmaps Work

1. **Hash Function**: Converts key to array index
2. **Storage**: Store value at that index
3. **Lookup**: Hash key, look up index, retrieve value

### 12.3. Hash Function Requirements

1. **Consistent**: Same key always produces same index
2. **Valid Range**: Index must be within array bounds
3. **Minimizes Collisions**: Different keys should hash to different indices

### 12.4. Simple Hashmap Implementation (Toy)

- **key_to_index(key)**: Sum Unicode values of characters: `total = sum(ord(c) for c in key)`, then `return total % len(self.hashmap)` so index is in range.
- **insert(key, value)**: `i = self.key_to_index(key)`, `self.hashmap[i] = (key, value)` (store key so we can iterate/print).
- **get(key)**: `i = self.key_to_index(key)`, `tup = self.hashmap[i]`; if tup is None raise exception; return `tup[1]` (the value).

**Quiz**: Hashmaps use **arrays** (or lists) under the hood. Big O to iterate over all keys and values? **O(n)** (must visit every bucket). Hashmaps map **hashable keys** to **any values**. In our toy hashmap, if "a" and "ba" are both used as keys they **collide** (same character sum). A good hashmap is **collision resistant**, has **efficient resizing**, and **uniform distribution**. Our toy allocates a large list even when not full → uses extra memory.

```python
class Hashmap:
    def __init__(self, size):
        self.hashmap = [None] * size
    
    def key_to_index(self, key):
        unicode_sum = sum(ord(char) for char in key)
        return unicode_sum % len(self.hashmap)
    
    def insert(self, key, value):
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)
    
    def get(self, key):
        index = self.key_to_index(key)
        pair = self.hashmap[index]
        if pair is None:
            raise KeyError(key)
        return pair[1]
```

### 12.5. Hashmap Operations

All **O(1)** on average:
- **Insert**: Hash key, store at index
- **Get**: Hash key, retrieve from index
- **Delete**: Hash key, remove from index

### 12.6. Limitations of Simple Hashmap

1. **Collisions**: Two keys hash to same index (overwrites)
2. **Memory Inefficient**: Allocates large array even for few items
3. **No Ordering**: Keys have no particular order
4. **No Range Queries**: Can't ask for "all keys between X and Y"

### 12.7. Production Hashmaps

Real implementations handle:
1. **Collision Resolution**: Open addressing, chaining, etc.
2. **Dynamic Resizing**: Grow array as needed
3. **Uniform Distribution**: Better hash functions

### 12.8. Real-World Use

**Use hashmaps constantly** for:
- Caching
- Lookups by ID
- Counting occurrences
- Quick existence checks

---

## 13. Tries

### 13.1. What is a Trie?

A trie (prefix tree) is a data structure that:
- Stores a set of strings
- Supports efficient prefix matching
- Uses nested dictionaries

### 13.2. Trie Structure

Each level represents a character position. Example trie with "hello", "help", "hi":

```
Root
├─ h
│  ├─ e
│  │  ├─ l
│  │  │  ├─ l
│  │  │  │  └─ o *
│  │  │  └─ p *
│  ├─ i *
```

The `*` marks where a complete word ends.

### 13.3. Trie Implementation

```python
class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'
    
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True
    
    def exists(self, word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return self.end_symbol in current
    
    def words_with_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current:
                return []
            current = current[char]
        
        words = []
        self.search_level(current, prefix, words)
        return words
    
    def search_level(self, level, prefix, words):
        if isinstance(level, bool):  # Reached a True (end marker) stored as value
            return words
        if self.end_symbol in level:
            words.append(prefix)
        for char in sorted(level.keys()):
            if char != self.end_symbol:
                self.search_level(level[char], prefix + char, words)
        return words
```

**words_with_prefix(prefix)**: Walk from root following prefix characters; if any missing return []. Then call search_level(current_level, prefix, []) to collect all complete words under that node.

### 13.4. find_matches(document)

Return set of all words in the trie that appear in the document (including as substrings/phrases). For each starting index i, walk the trie with document[i], document[i+1], ...; if we hit end_symbol, add document[i:j+1] to matches. Handles phrases and substrings (unlike splitting on spaces and using a set).

```python
def find_matches(self, document):
    matches = set()
    for i in range(len(document)):
        level = self.root
        for j in range(i, len(document)):
            c = document[j]
            if c not in level:
                break
            level = level[c]
            if self.end_symbol in level:
                matches.add(document[i:j+1])
    return matches
```

**Big O find_matches**: O(n × m) where n = document length, m = average depth of trie (we break early often). Not O(n²) because inner loop breaks. **Why not just dictionary?** Tries match substrings and multi-word phrases; a dictionary would need every possible substring.

### 13.5. Trie Operations

- **Insert**: O(m) where m = word length
- **Search (exists)**: O(m) where m = **length of the word** (not number of words in trie)
- **Prefix Match**: O(m + k) where k = words with prefix

**Quiz**: Hashmaps can be used for suffix matching, prefix matching, exact matching? — **Exact matching only**. Tries support prefix (and exact).

### 13.6. Real-World Uses

1. **Autocomplete**: Find words starting with prefix
2. **Spell Checking**: Find similar words
3. **IP Routing**: Match IP prefixes
4. **Dictionary**: Store all dictionary words
5. **Bad Word Filtering**: Match profanity patterns

**Example**: Autocomplete for "dev" returns ["developer", "development", "devops"]

---

## 14. Graphs

### 14.1. What is a Graph?

A graph is a data structure with:
- **Vertices (Nodes)**: The entities
- **Edges**: Connections between vertices

Unlike trees, vertices can have multiple parents and arbitrary connections.

### 14.2. Graph Representations

**Adjacency Matrix**: 2D array where matrix[i][j] = true if edge exists

```python
# Example: Complete graph with 3 vertices
matrix = [
    [False, True, True],
    [True, False, True],
    [True, True, False]
]
```

**Adjacency List**: Dictionary where key maps to set of connected vertices

```python
graph = {
    0: {1, 2},
    1: {0, 2},
    2: {0, 1}
}
```

### 14.3. Graph Implementation (Adjacency Matrix)

- **init(num_vertices)**: `self.graph = [[False]*num_vertices for _ in range(num_vertices)]`.
- **add_edge(u, v)**: For undirected graph set both `self.graph[u][v] = True` and `self.graph[v][u] = True`. Optionally guard: if u or v out of bounds, return.

### 14.4. Graph Quiz

- **Graphs must have a root vertex?** **No** (unlike trees).
- **Maximum edges (undirected)** with n vertices: **n(n-1)/2** (slightly less than half of n²). For 2 vertices: 1; 3 vertices: 3; 4 vertices: 6. Complete graph with 6 vertices: 15 edges.
- **Adjacency list — how is absence of edge represented?** The node's list/set **does not contain** that other node (no "false" in list; we use sets/lists of neighbors only).
- **Best stored as**: Dictionary of vertices mapping to **set** of vertices (no order needed).

### 14.5. Graph Implementation (Adjacency List)

```python
class Graph:
    def __init__(self, num_vertices):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        if v not in self.graph:
            self.graph[v] = set()
        
        self.graph[u].add(v)
        self.graph[v].add(u)
```

### 14.6. Real-World Uses

1. **Social Networks**: Users as vertices, friendships as edges
2. **Road Maps**: Cities as vertices, roads as edges
3. **Computer Networks**: Computers as vertices, connections as edges
4. **Game AI**: States as vertices, possible actions as edges
5. **Web Crawling**: Pages as vertices, hyperlinks as edges

### 14.7. Complete Graph

A complete graph where every pair of vertices is connected:
- n vertices → n×(n-1)/2 edges maximum

---

## 15. Breadth-First Search (BFS)

### 15.1. What is BFS?

Breadth-first search explores a graph level-by-level:
- Start at a vertex
- Visit all neighbors first
- Then visit neighbors of neighbors
- Continue until all reachable vertices visited

### 15.2. BFS Algorithm

1. Create a queue and add start vertex
2. While queue is not empty:
   - Remove vertex from front
   - Mark as visited
   - Add unvisited neighbors to back of queue

### 15.3. BFS Implementation

- **Queue**: Use a list: add with `to_explore.append(neighbor)`, remove from front with `next_vertex = to_explore[0]` then `del to_explore[0]` (or `pop(0)`).
- **Critical bug**: When fetching neighbors, use the **current** vertex (`next_vertex`), not the start vertex. So `neighbors = sorted(graph[next_vertex])`. Otherwise every node gets the same neighbors and you miss vertices (e.g. Dubai).

```python
def breadth_first_search(graph, start):
    visited = []
    to_explore = [start]
    
    while len(to_explore) > 0:
        next_vertex = to_explore[0]
        del to_explore[0]
        visited.append(next_vertex)
        
        neighbors = sorted(graph[next_vertex])  # Use next_vertex, not start!
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in to_explore:
                to_explore.append(neighbor)
    
    return visited
```

### 15.4. BFS Complexity

- **Time**: O(V + E) where V = vertices, E = edges
- **Space**: O(V) for queue storage

### 15.5. When to Use BFS

1. **Shortest Path**: Find shortest path in unweighted graph
2. **Close Neighbors**: Solution likely near start
3. **Web Crawling**: Visit pages level-by-level
4. **Small Memory**: Better than DFS for wide graphs

### 15.6. BFS Disadvantages

- Uses more memory (stores entire level)
- Not good for deep solution spaces

---

## 16. Depth-First Search (DFS)

### 16.1. What is DFS?

Depth-first search explores a graph by going deep:
- Start at a vertex
- Go as far as possible down one branch
- Backtrack and try another branch
- Continue until all reachable vertices visited

### 16.2. DFS Algorithm (Recursive)

1. Visit current vertex
2. For each unvisited neighbor:
   - Recursively visit that neighbor
3. Backtrack when no more neighbors

### 16.3. DFS Implementation

- **Common bug**: Append the **current vertex** to the visited list: `visited.append(vertex)`, not something like `visited.append(visited)` (which would cause "argument of type bool is not iterable" or wrong structure). Recursion stops when all neighbors are already in visited.

```python
def depth_first_search(graph, start):
    visited = []
    depth_first_search_recursive(graph, start, visited)
    return visited

def depth_first_search_recursive(graph, vertex, visited):
    visited.append(vertex)
    
    neighbors = sorted(graph[vertex])
    for neighbor in neighbors:
        if neighbor not in visited:
            depth_first_search_recursive(graph, neighbor, visited)
```

**Quiz**: Solution likely very shallow in a tree-based graph → **BFS**. Search space has infinite depth → **BFS** (DFS might never return). Use less memory in a very wide graph → **DFS** (BFS stores whole level in queue).

### 16.4. DFS Complexity

- **Time**: O(V + E) same as BFS
- **Space**: O(V) for recursion stack (better than BFS on wide graphs)

### 16.5. When to Use DFS

1. **Deep Solutions**: Solution likely far from start
2. **Memory Constrained**: Uses less memory than BFS
3. **Path Finding**: Find any path (not necessarily shortest)

### 16.6. DFS Disadvantages

- Uses recursion (call stack overhead)
- Can hit infinite recursion on cycles
- Doesn't find shortest path

---

## 17. P vs NP

### 17.1. Complexity Classes

**P (Polynomial Time)**: Problems solvable in polynomial time
- O(n), O(n log n), O(n²), etc.
- Practical to solve on computers
- Examples: Sorting, searching

**NP (Non-Deterministic Polynomial)**: Problems verifiable in polynomial time
- Solution can be checked quickly
- But solution might take exponential time to find
- Examples: Traveling salesman, factorization

### 17.2. Key Insight

**Hard to Solve, Easy to Verify**

Example: Traveling Salesman Problem
- **Solving**: Try all routes → O(n!) time (exponential)
- **Verifying**: Check given route → O(n) time (polynomial)

If someone says "here's a route with distance < 100", you can quickly verify it's correct.

### 17.3. The P vs NP Question

**The Question**: Does P = NP?

Are all problems that are easy to verify also easy to solve?

**Current Status**:
- Not proven either way
- $1 million prize for proof
- Strongly suspected P ≠ NP (probably not equal)
- If P = NP, cryptography would break

### 17.4. Why It Matters

If someone solves **one** NP-complete problem in polynomial time:
- ALL NP problems become solvable in polynomial time
- Modern encryption would break
- Massive implications for security

### 17.5. NP-Complete Problems

Some problems have special property: all other NP problems can be reduced to them.

**Traveling Salesman (TSP)**:
- **Problem**: Given cities, distances between pairs, and a distance limit — is there a path visiting each city once with total distance < limit?
- **Solving**: Try all permutations of cities; for each permutation sum the distances (paths[perm[i-1]][perm[i]]); if any total < dist return True; else False. **O(n!)**.
- **Verifying**: Given a path, sum distances between consecutive cities; return total < dist. **O(n)** — polynomial.

```python
def tsp(cities, paths, dist):
    from itertools import permutations
    for perm in permutations(cities):
        total = 0
        for i in range(1, len(perm)):
            total += paths[perm[i-1]][perm[i]]
        if total < dist:
            return True
    return False

def verify_tsp(paths, dist, path):
    total = 0
    for i in range(1, len(path)):
        total += paths[path[i-1]][path[i]]
    return total < dist
```

**Quiz**: Big O of TSP and verify_tsp — **factorial** and **linear** respectively. TSP is in **NP** (verifiable in polynomial time; solving not in P).

### 17.6. Password Guessing (get_num_guesses)

- **Input**: Password length (max length to try).
- **Assumption**: 26 lowercase letters; brute force tries all passwords of length 1, then 2, ... up to given length.
- **Number of guesses**: 26^1 + 26^2 + ... + 26^length = sum(26**(i+1) for i in range(length)), or use formula for geometric series. Exponential in length — "slow to solve, fast to verify" (verify = compare one string).

### 17.7. NP-Hard vs NP-Complete

**NP-Complete**: 
- Must be in NP (verifiable in polynomial time)
- All NP problems reduce to it in polynomial time
- **All NP-complete problems are also NP-hard**

**NP-Hard**:
- Every problem in NP can be reduced to it in polynomial time
- Does **not** have to be in NP (might not be verifiable in poly time)
- Not all NP-hard problems are NP-complete

**Quiz**: P is **subset** of NP (everything solvable in poly time is also verifiable in poly time). NP is **superset** of P. Problems in NP can be **verified** in polynomial time. If we find a polynomial-time solution to one NP-complete problem → **all NP problems** can be solved in polynomial time (P = NP). What happens if we find poly-time solution to an NP-complete problem? **We learn that P = NP** (and cryptography is in trouble). Does P equal NP? **We don't know, but probably not.** Is it simpler to prove P = NP or P ≠ NP? **P = NP** (just need one poly-time algorithm for an NP-complete problem; proving P ≠ NP requires showing no such algorithm exists).

### 17.8. Real-World Example: Password Verification

- **Guessing**: O(26^n) - exponential, impractical
- **Verifying**: O(1) - constant, instant

This is why we can't easily break passwords despite them being "just" data.

---

## 18. Prime Factorization

### 18.1. The Problem

**Factorization**: Given a large number, find its prime factors.

**Example**:
- 8 → [2, 2, 2]
- 10 → [2, 5]
- 24 → [2, 2, 2, 3]

### 18.2. Factorization Algorithm

- Divide n by 2 as many times as possible (while n % 2 == 0), appending 2 each time; then n is odd.
- Loop i = 3, 5, 7, ... up to √n (inclusive). For each i, **while** n % i == 0: append i, n = n // i (nested loop until i doesn't divide evenly). Then move to next i.
- If after the loop n > 2, then n is prime — append n.
- Return list of integers (prime factors from least to greatest).

```python
import math

def prime_factors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    if n > 2:
        factors.append(n)
    
    return factors
```

### 18.3. Complexity Analysis

**By Number n**: O(√n) — first loop O(log n) for factors of 2; second loop runs up to √n. So **O(√n)** with respect to the integer n (looks polynomial in n).

**By Bits s**: Input size in computer science is often measured in **bits**. If n has s bits, then n ≈ 2^s, so √n ≈ 2^(s/2). So complexity in terms of s is **O(2^(s/2))** — **exponential** in the input size (bits). This is why factoring is considered hard.

**Why Bits Matter**: 
- Encryption keys are 256+ bits
- By bits, this is exponential → impractical to crack

**Quiz**: Prime factorization is definitely part of **NP** (easy to verify: multiply factors). Given two large primes and their product, can we verify in polynomial time? **Yes** (multiplication is poly time).

### 18.4. Cryptography Implication

Modern encryption (RSA) relies on:
- Easy to multiply two primes: P × Q = N
- Hard to factor N back to P and Q

If efficient factorization discovered → encryption breaks!

### 18.5. P vs NP Implication

- **Factoring**: NP (easy to verify: P × Q = N)
- **Probably not in P** (no polynomial algorithm found)
- If proven NP-complete and polynomial solution found → P = NP

---

## 19. Summary

### 19.1. Key Takeaways

1. **Algorithms Matter**: Choose right algorithm for performance
2. **Big O Guides Decisions**: O(log n) better than O(n²)
3. **Data Structures Enable Algorithms**: Right structure = right performance
4. **Trade-offs Exist**: Space vs time, complexity vs simplicity
5. **Real-World Uses**: Sort → search → tree structures → problems

### 19.2. Complexity Classes Quick Reference

| Big O | Time | Use Case |
|-------|------|----------|
| O(1) | Constant | Direct access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single pass |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops (avoid) |
| O(2^n) | Exponential | Power sets (very slow) |
| O(n!) | Factorial | Permutations (impractical) |

### 19.3. Further Learning

- Practice implementing all data structures from scratch
- Solve problems on LeetCode/HackerRank
- Understand tradeoffs between algorithms
- Study how real systems use these concepts
- Learn about P vs NP problem more deeply

---
End-of-File

The [KintsugiStack](https://github.com/kintsugi-programmer/KintsugiStack) repository, authored by Kintsugi-Programmer, is less a comprehensive resource and more an Artifact of Continuous Research and Deep Inquiry into Computer Science and Software Engineering. It serves as a transparent ledger of the author's relentless pursuit of mastery, from the foundational algorithms to modern full-stack implementation.

> Made with 💚 [Kintsugi-Programmer](https://github.com/kintsugi-programmer)
