"""
10 Common Python  Coding Functions
Covering basic to advanced skill levels
"""

# 1. PALINDROME CHECK (Basic)
def is_palindrome(s):
    """
    Check if a string is a palindrome (reads same forwards and backwards)
    Time Complexity: O(n), Space Complexity: O(1)
    """
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# 2. REVERSE STRING (Basic)
def reverse_string(s):
    """
    Reverse a string using different methods
    Time Complexity: O(n), Space Complexity: O(n)
    """
    # Method 1: Using slicing
    return s[::-1]
    # Method 2: Using loop
    # return ''.join(reversed(s))


# 3. FIBONACCI SEQUENCE (Basic-Intermediate)
def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms using recursion
    Time Complexity: O(2^n) - naive recursion, Space Complexity: O(n)
    """
    def fib_recursive(num):
        """Helper function to calculate nth Fibonacci number recursively"""
        if num <= 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib_recursive(num - 1) + fib_recursive(num - 2)
    
    if n <= 0:
        return []
    
    return [fib_recursive(i) for i in range(n)]


# 4. TWO SUM PROBLEM (Intermediate)
def two_sum(nums, target):
    """
    Find two numbers that add up to target
    Returns indices of the two numbers
    Time Complexity: O(n), Space Complexity: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


# 5. FIND DUPLICATES IN ARRAY (Intermediate)
def find_duplicates(arr):
    """
    Find all duplicate elements in an array
    Time Complexity: O(n), Space Complexity: O(n)
    """
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)


# 6. ANAGRAM CHECK (Basic-Intermediate)
def is_anagram(s1, s2):
    """
    Check if two strings are anagrams
    Time Complexity: O(n log n), Space Complexity: O(1)
    """
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    return sorted(s1) == sorted(s2)


# 7. FIZZBUZZ (Basic)
def fizzbuzz(n):
    """
    Classic FizzBuzz problem - print numbers 1 to n
    Replace multiples of 3 with "Fizz", 5 with "Buzz", both with "FizzBuzz"
    Time Complexity: O(n), Space Complexity: O(n)
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# 8. BINARY SEARCH (Intermediate)
def binary_search(arr, target):
    """
    Binary search in a sorted array
    Returns index of target if found, -1 otherwise
    Time Complexity: O(log n), Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# 9. FIND MISSING NUMBER (Intermediate-Advanced)
def find_missing_number(arr):
    """
    Find missing number in array containing n distinct numbers from 0 to n
    Time Complexity: O(n), Space Complexity: O(1)
    Uses mathematical formula: sum of n numbers - sum of array
    """
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


# 10. ROTATE ARRAY (Advanced)
def rotate_array(arr, k):
    """
    Rotate array to the right by k steps
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if not arr or k == 0:
        return arr
    
    n = len(arr)
    k = k % n  # Handle k > n
    
    # Reverse entire array
    arr.reverse()
    # Reverse first k elements
    arr[:k] = reversed(arr[:k])
    # Reverse remaining elements
    arr[k:] = reversed(arr[k:])
    
    return arr


# TEST FUNCTIONS
def test_all_functions():
    """Test all interview functions with sample inputs"""
    
    print("=" * 60)
    print("TESTING 10 PYTHON INTERVIEW FUNCTIONS")
    print("=" * 60)
    
    # Test 1: Palindrome
    print("\n1. PALINDROME CHECK")
    print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
    print(f"is_palindrome('hello'): {is_palindrome('hello')}")
    print(f"is_palindrome('A man a plan a canal Panama'): {is_palindrome('A man a plan a canal Panama')}")
    
    # Test 2: Reverse String
    print("\n2. REVERSE STRING")
    print(f"reverse_string('hello'): {reverse_string('hello')}")
    print(f"reverse_string('Python'): {reverse_string('Python')}")
    
    # Test 3: Fibonacci
    print("\n3. FIBONACCI SEQUENCE")
    print(f"fibonacci(10): {fibonacci(10)}")
    print(f"fibonacci(7): {fibonacci(7)}")
    
    # Test 4: Two Sum
    print("\n4. TWO SUM PROBLEM")
    print(f"two_sum([2, 7, 11, 15], 9): {two_sum([2, 7, 11, 15], 9)}")
    print(f"two_sum([3, 2, 4], 6): {two_sum([3, 2, 4], 6)}")
    
    # Test 5: Find Duplicates
    print("\n5. FIND DUPLICATES")
    print(f"find_duplicates([1, 2, 3, 2, 4, 5, 3]): {find_duplicates([1, 2, 3, 2, 4, 5, 3])}")
    print(f"find_duplicates([1, 1, 1, 2, 2, 3]): {find_duplicates([1, 1, 1, 2, 2, 3])}")
    
    # Test 6: Anagram
    print("\n6. ANAGRAM CHECK")
    print(f"is_anagram('listen', 'silent'): {is_anagram('listen', 'silent')}")
    print(f"is_anagram('hello', 'world'): {is_anagram('hello', 'world')}")
    
    # Test 7: FizzBuzz
    print("\n7. FIZZBUZZ")
    print(f"fizzbuzz(15): {fizzbuzz(15)}")
    
    # Test 8: Binary Search
    print("\n8. BINARY SEARCH")
    print(f"binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5): {binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)}")
    print(f"binary_search([1, 2, 3, 4, 5], 10): {binary_search([1, 2, 3, 4, 5], 10)}")
    
    # Test 9: Find Missing Number
    print("\n9. FIND MISSING NUMBER")
    print(f"find_missing_number([0, 1, 3, 4, 5]): {find_missing_number([0, 1, 3, 4, 5])}")
    print(f"find_missing_number([0, 1, 2, 3, 4, 5, 7]): {find_missing_number([0, 1, 2, 3, 4, 5, 7])}")
    
    # Test 10: Rotate Array
    print("\n10. ROTATE ARRAY")
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    print(f"rotate_array([1, 2, 3, 4, 5, 6, 7], 3): {rotate_array(arr1.copy(), 3)}")
    arr2 = [1, 2, 3, 4, 5]
    print(f"rotate_array([1, 2, 3, 4, 5], 2): {rotate_array(arr2.copy(), 2)}")
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)


def main():
    """Main function to run tests"""
    test_all_functions()


if __name__ == "__main__":
    main()
