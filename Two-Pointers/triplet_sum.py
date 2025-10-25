def triplet_sum(lst):
    """
    Find all unique triplets in the array that sum to zero.
    
    Time Complexity: O(n²)
    Space Complexity: O(1) auxiliary space
    
    Args:
        lst: List of integers
    
    Returns:
        List of triplets that sum to zero
    """
    if len(lst) < 3:
        return []
    
    triplets = []
    lst.sort()  # O(n log n)
    
    for i in range(len(lst) - 2):  # Fix the first element
        # Skip positive numbers as first element (optimization)
        if lst[i] > 0:
            break
            
        # Skip duplicates for the first element
        if i > 0 and lst[i] == lst[i - 1]:
            continue
        
        # Two pointers for remaining elements
        left = i + 1
        right = len(lst) - 1
        
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            
            if current_sum == 0:
                triplets.append([lst[i], lst[left], lst[right]])
                
                # Skip duplicates for left pointer
                while left < right and lst[left] == lst[left + 1]:
                    left += 1
                # Skip duplicates for right pointer  
                while left < right and lst[right] == lst[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif current_sum < 0:
                left += 1  # Need larger sum
            else:
                right -= 1  # Need smaller sum
    
    return triplets


def triplet_sum_optimized(lst):
    """
    Alternative implementation with additional optimizations.
    
    Time Complexity: O(n²)
    Space Complexity: O(1) auxiliary space
    """
    if len(lst) < 3:
        return []
    
    triplets = []
    lst.sort()
    
    for i in range(len(lst) - 2):
        # Early termination: if smallest element > 0, no triplet can sum to 0
        if lst[i] > 0:
            break
            
        # Skip duplicates
        if i > 0 and lst[i] == lst[i - 1]:
            continue
            
        # Early termination: if current triplet minimum > 0
        if lst[i] + lst[i + 1] + lst[i + 2] > 0:
            break
            
        # Early termination: if current triplet maximum < 0
        if lst[i] + lst[-2] + lst[-1] < 0:
            continue
        
        left, right = i + 1, len(lst) - 1
        
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            
            if current_sum == 0:
                triplets.append([lst[i], lst[left], lst[right]])
                
                # Skip all duplicates
                while left < right and lst[left] == lst[left + 1]:
                    left += 1
                while left < right and lst[right] == lst[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return triplets


def test_triplet_implementations():
    """Test both implementations with various test cases."""
    test_cases = [
        [0, -1, 2, -3, 1],           # Original test case
        [-1, 0, 1, 2, -1, -4],       # Multiple triplets
        [-2, 0, 1, 1, 2],            # Duplicates
        [0, 0, 0, 0],                # All zeros
        [1, 2, 3],                   # No solution
        [-1, -1, 2],                 # Single solution
        [],                          # Empty array
        [1, 2]                       # Less than 3 elements
    ]
    
    print("Testing Triplet Sum Implementations")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases):
        print(f"\nTest Case {i+1}: {test_case}")
        
        result1 = triplet_sum(test_case.copy())
        result2 = triplet_sum_optimized(test_case.copy())
        
        print(f"Standard:  {result1}")
        print(f"Optimized: {result2}")
        print(f"Match: {result1 == result2}")


def performance_comparison():
    """Compare performance of both implementations."""
    import time
    import random
    
    # Generate test data
    sizes = [50, 100, 200]
    
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    for size in sizes:
        # Generate random test data
        test_data = [random.randint(-size, size) for _ in range(size)]
        
        print(f"\nArray size: {size}")
        print("-" * 30)
        
        # Test standard implementation
        start_time = time.time()
        result1 = triplet_sum(test_data.copy())
        time1 = time.time() - start_time
        
        # Test optimized implementation  
        start_time = time.time()
        result2 = triplet_sum_optimized(test_data.copy())
        time2 = time.time() - start_time
        
        print(f"Standard implementation:  {time1:.6f}s ({len(result1)} triplets)")
        print(f"Optimized implementation: {time2:.6f}s ({len(result2)} triplets)")
        print(f"Speedup: {time1/time2:.2f}x" if time2 > 0 else "N/A")
        print(f"Results match: {set(map(tuple, result1)) == set(map(tuple, result2))}")


if __name__ == "__main__":
    test_triplet_implementations()
    performance_comparison()