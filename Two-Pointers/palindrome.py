def palindrome_original(word):
    """
    Original implementation with list comprehension.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - creates a new list
    """
    if len(word) > 0:
        lst = ([w.lower() for w in word if w.isalnum()])
        
        i = 0
        j = len(lst) - 1

        while i < j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1
        return True
    return True


def palindrome_optimized(word):
    """
    Space-optimized implementation using two pointers directly on string.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - no extra space needed
    """
    if not word:
        return True
    
    left = 0
    right = len(word) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not word[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric characters from right
        while left < right and not word[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if word[left].lower() != word[right].lower():
            return False
            
        left += 1
        right -= 1
    
    return True


def palindrome_pythonic(word):
    """
    Pythonic implementation using string methods.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - creates cleaned string
    """
    # Remove non-alphanumeric and convert to lowercase
    cleaned = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned == cleaned[::-1]


def palindrome_regex(word):
    """
    Implementation using regex for cleaning.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - creates cleaned string
    """
    import re
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
    return cleaned == cleaned[::-1]


# Alias for backward compatibility
palindrome = palindrome_optimized


def test_palindrome_implementations():
    """Test all palindrome implementations with various test cases."""
    test_cases = [
        ("", True),                                    # Empty string
        ("a", True),                                  # Single character
        ("A man a plan a canal Panama", True),        # Classic palindrome
        ("race a car", False),                        # Not a palindrome
        ("a dog! a panic in a pagoda.", True),        # Original test case
        ("Madam", True),                              # Case sensitivity
        ("No 'x' in Nixon", True),                    # Complex punctuation
        ("12321", True),                              # Numeric palindrome
        ("12345", False),                             # Not numeric palindrome
        ("A Santa at NASA", True),                    # Mixed case
        ("Was it a car or a cat I saw?", True),       # Question marks
        ("12345abcde54321", False),                   # Mixed alphanumeric
        ("Abc3cbA", True),                            # Mixed with numbers
    ]
    
    implementations = [
        ("Original", palindrome_original),
        ("Optimized", palindrome_optimized),
        ("Pythonic", palindrome_pythonic),
        ("Regex", palindrome_regex)
    ]
    
    print("Testing Palindrome Implementations")
    print("=" * 50)
    
    for i, (test_input, expected) in enumerate(test_cases):
        print(f"\nTest Case {i+1}: '{test_input}' -> Expected: {expected}")
        
        all_match = True
        results = {}
        
        for name, func in implementations:
            try:
                result = func(test_input)
                results[name] = result
                if result != expected:
                    all_match = False
                    print(f"  ❌ {name}: {result}")
                else:
                    print(f"  ✅ {name}: {result}")
            except Exception as e:
                print(f"  ❌ {name}: ERROR - {e}")
                all_match = False
        
        if all_match:
            print("  🎉 All implementations agree!")


def performance_comparison():
    """Compare performance of different palindrome implementations."""
    import time
    
    # Test data of varying sizes
    test_strings = [
        "A man a plan a canal Panama" * 10,          # ~270 chars
        "race a car! " * 50,                         # ~600 chars  
        "Was it a car or a cat I saw? " * 100,       # ~3000 chars
        "12321abcde" * 500,                          # ~5000 chars
    ]
    
    implementations = [
        ("Original", palindrome_original),
        ("Optimized", palindrome_optimized), 
        ("Pythonic", palindrome_pythonic),
        ("Regex", palindrome_regex)
    ]
    
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    for i, test_string in enumerate(test_strings):
        print(f"\nTest String {i+1} (Length: {len(test_string)} chars)")
        print("-" * 40)
        
        results = {}
        times = {}
        
        for name, func in implementations:
            # Warm up
            for _ in range(10):
                func(test_string)
            
            # Measure performance
            start_time = time.perf_counter()
            for _ in range(1000):  # Run multiple times for better measurement
                result = func(test_string)
            end_time = time.perf_counter()
            
            avg_time = (end_time - start_time) / 1000
            results[name] = result
            times[name] = avg_time
            
            print(f"{name:12}: {avg_time*1000000:.2f} μs/call -> {result}")
        
        # Find fastest
        fastest = min(times.items(), key=lambda x: x[1])
        print(f"\nFastest: {fastest[0]} ({fastest[1]*1000000:.2f} μs)")
        
        # Calculate speedups
        base_time = times["Original"]
        for name, time_taken in times.items():
            if name != "Original":
                speedup = base_time / time_taken
                print(f"{name} vs Original: {speedup:.2f}x {'faster' if speedup > 1 else 'slower'}")


def memory_analysis():
    """Analyze memory usage of different implementations."""
    import sys
    
    test_string = "A man a plan a canal Panama! " * 100  # ~3000 chars
    
    print("\n" + "=" * 60)
    print("MEMORY ANALYSIS")
    print("=" * 60)
    
    def get_size_mb(obj):
        return sys.getsizeof(obj) / 1024 / 1024
    
    print(f"Input string size: {get_size_mb(test_string):.4f} MB")
    print(f"Input string length: {len(test_string)} characters")
    
    # Original implementation memory usage
    print(f"\nOriginal Implementation:")
    lst = [w for w in test_string if w.isalnum()]
    print(f"  Filtered list size: {get_size_mb(lst):.4f} MB")
    print(f"  Filtered list length: {len(lst)} characters")
    print(f"  Memory overhead: {get_size_mb(lst) / get_size_mb(test_string):.2f}x")
    
    # Pythonic implementation memory usage  
    print(f"\nPythonic Implementation:")
    cleaned = ''.join(char.lower() for char in test_string if char.isalnum())
    print(f"  Cleaned string size: {get_size_mb(cleaned):.4f} MB")
    print(f"  Reversed string size: {get_size_mb(cleaned[::-1]):.4f} MB")
    print(f"  Total memory overhead: {(get_size_mb(cleaned) * 2) / get_size_mb(test_string):.2f}x")
    
    print(f"\nOptimized Implementation:")
    print(f"  Additional memory: ~0 MB (O(1) space complexity)")


if __name__ == "__main__":
    # Test the original case
    print("Original test case:")
    print(f"palindrome('a dog! a panic in a pagoda.') = {palindrome('a dog! a panic in a pagoda.')}")
    
    # Run comprehensive tests
    test_palindrome_implementations()
    performance_comparison()
    memory_analysis()

'''
Original test case:
palindrome('a dog! a panic in a pagoda.') = True
Testing Palindrome Implementations
==================================================

Test Case 1: '' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 2: 'a' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 3: 'A man a plan a canal Panama' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 4: 'race a car' -> Expected: False
  ✅ Original: False
  ✅ Optimized: False
  ✅ Pythonic: False
  ✅ Regex: False
  🎉 All implementations agree!

Test Case 5: 'a dog! a panic in a pagoda.' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 6: 'Madam' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 7: 'No 'x' in Nixon' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 8: '12321' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 9: '12345' -> Expected: False
  ✅ Original: False
  ✅ Optimized: False
  ✅ Pythonic: False
  ✅ Regex: False
  🎉 All implementations agree!

Test Case 10: 'A Santa at NASA' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 11: 'Was it a car or a cat I saw?' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

Test Case 12: '12345abcde54321' -> Expected: False
  ✅ Original: False
  ✅ Optimized: False
  ✅ Pythonic: False
  ✅ Regex: False
  🎉 All implementations agree!

Test Case 13: 'Abc3cbA' -> Expected: True
  ✅ Original: True
  ✅ Optimized: True
  ✅ Pythonic: True
  ✅ Regex: True
  🎉 All implementations agree!

============================================================
PERFORMANCE COMPARISON
============================================================

Test String 1 (Length: 270 chars)
----------------------------------------
Original    : 25.34 μs/call -> True
Optimized   : 31.77 μs/call -> True
Pythonic    : 21.44 μs/call -> True
Regex       : 10.07 μs/call -> True

Fastest: Regex (10.07 μs)
Optimized vs Original: 0.80x slower
Pythonic vs Original: 1.18x faster
Regex vs Original: 2.52x faster

Test String 2 (Length: 600 chars)
----------------------------------------
Original    : 29.15 μs/call -> False
Optimized   : 1.13 μs/call -> False
Pythonic    : 51.22 μs/call -> False
Regex       : 27.53 μs/call -> False

Fastest: Optimized (1.13 μs)
Optimized vs Original: 25.91x faster
Pythonic vs Original: 0.57x slower
Regex vs Original: 1.06x faster

Test String 3 (Length: 2900 chars)
----------------------------------------
Original    : 191.16 μs/call -> True
Optimized   : 338.72 μs/call -> True
Pythonic    : 181.85 μs/call -> True
Regex       : 139.04 μs/call -> True

Fastest: Regex (139.04 μs)
Optimized vs Original: 0.56x slower
Pythonic vs Original: 1.05x faster
Regex vs Original: 1.37x faster

Test String 4 (Length: 5000 chars)
----------------------------------------
Original    : 284.34 μs/call -> False
Optimized   : 0.37 μs/call -> False
Pythonic    : 385.00 μs/call -> False
Regex       : 27.97 μs/call -> False

Fastest: Optimized (0.37 μs)
Optimized vs Original: 760.77x faster
Pythonic vs Original: 0.74x slower
Regex vs Original: 10.17x faster

============================================================
MEMORY ANALYSIS
============================================================
Input string size: 0.0028 MB
Input string length: 2900 characters

Original Implementation:
  Filtered list size: 0.0174 MB
  Filtered list length: 2100 characters
  Memory overhead: 6.20x

Pythonic Implementation:
  Cleaned string size: 0.0020 MB
  Reversed string size: 0.0020 MB
  Total memory overhead: 1.46x

Optimized Implementation:
  Additional memory: ~0 MB (O(1) space complexity)
'''