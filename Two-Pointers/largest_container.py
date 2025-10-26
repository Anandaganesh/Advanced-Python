def largest_container_original(heights):
    """
    Original implementation (has logic issues).
    
    Issues:
    - Incorrect pointer movement logic
    - Can miss optimal solutions
    - May cause index out of bounds errors
    """
    if len(heights) > 1:
        i = 0
        j = len(heights) - 1
        largest_container = (min(heights[i], heights[j])) * ((j - i))
        container = min(heights[i], heights[j])
        
        while i < j:
            if container == heights[i]:
                i += 1
            elif container == heights[j]:
                j -= 1
            
            if i < j:  # Add bounds check
                container = min(heights[i], heights[j])
                if (min(heights[i], heights[j])) * (j-i) > largest_container:
                    largest_container = (min(heights[i], heights[j])) * (j-i)
        return largest_container
    return 0


def largest_container_optimal(heights):
    """
    Optimal two-pointer solution for Container With Most Water problem.
    
    Algorithm:
    1. Start with two pointers at the beginning and end
    2. Calculate area with current pointers
    3. Move the pointer with smaller height inward
    4. Repeat until pointers meet
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Why this works:
    - We always move the pointer with smaller height because:
      - Moving the taller pointer can only decrease the area
      - Moving the shorter pointer might increase the area
    """
    if len(heights) < 2:
        return 0
    
    left = 0
    right = len(heights) - 1
    max_area = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        height = min(heights[left], heights[right])
        current_area = width * height
        
        # Update maximum area
        max_area = max(max_area, current_area)
        
        # Move the pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def largest_container_brute_force(heights):
    """
    Brute force solution for comparison.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    if len(heights) < 2:
        return 0
    
    max_area = 0
    n = len(heights)
    
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            height = min(heights[i], heights[j])
            area = width * height
            max_area = max(max_area, area)
    
    return max_area


def largest_container_with_indices(heights):
    """
    Returns both the maximum area and the indices that produce it.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(heights) < 2:
        return 0, (-1, -1)
    
    left = 0
    right = len(heights) - 1
    max_area = 0
    best_indices = (0, len(heights) - 1)
    
    while left < right:
        # Calculate current area
        width = right - left
        height = min(heights[left], heights[right])
        current_area = width * height
        
        # Update maximum area and indices
        if current_area > max_area:
            max_area = current_area
            best_indices = (left, right)
        
        # Move the pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area, best_indices


# Alias for the optimal solution
largest_container = largest_container_optimal

def test_implementations():
    """Test all implementations with various test cases."""
    test_cases = [
        ([2, 7, 8, 3, 7, 6], 35),           # Original test case
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), # LeetCode example
        ([1, 1], 1),                        # Minimum case
        ([4, 3, 2, 1, 4], 16),             # Symmetric case
        ([1, 2, 1], 2),                     # Small case
        ([2, 1], 1),                        # Two elements
        ([5], 0),                           # Single element
        ([], 0),                            # Empty array
        ([1, 2, 4, 3], 4),                  # Example with multiple solutions
        ([6, 4, 3, 1, 4, 6, 99], 36),      # High peak in middle
        ([1, 2, 3, 4, 5], 6),              # Ascending
        ([5, 4, 3, 2, 1], 6),              # Descending
    ]
    
    implementations = [
        ("Brute Force", largest_container_brute_force),
        ("Optimal", largest_container_optimal),
        ("With Indices", lambda x: largest_container_with_indices(x)[0]),
    ]
    
    print("Testing Container With Most Water Implementations")
    print("=" * 60)
    
    for i, (heights, expected) in enumerate(test_cases):
        print(f"\nTest Case {i+1}: {heights}")
        print(f"Expected: {expected}")
        
        all_correct = True
        for name, func in implementations:
            try:
                result = func(heights.copy())
                status = "✅" if result == expected else "❌"
                print(f"  {status} {name:15}: {result}")
                if result != expected:
                    all_correct = False
            except Exception as e:
                print(f"  ❌ {name:15}: ERROR - {e}")
                all_correct = False
        
        if all_correct:
            print("  🎉 All implementations correct!")
        
        # Show detailed solution for interesting cases
        if len(heights) > 2:
            area, indices = largest_container_with_indices(heights)
            if indices != (-1, -1):
                left_idx, right_idx = indices
                print(f"  📍 Best container: indices ({left_idx}, {right_idx}) "
                      f"heights ({heights[left_idx]}, {heights[right_idx]}) "
                      f"width {right_idx - left_idx} = area {area}")


def performance_comparison():
    """Compare performance of different implementations."""
    import time
    import random
    
    # Generate test data of varying sizes
    sizes = [50, 100, 500, 1000]
    
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    implementations = [
        ("Brute Force O(n²)", largest_container_brute_force),
        ("Optimal O(n)", largest_container_optimal),
    ]
    
    for size in sizes:
        print(f"\nArray size: {size}")
        print("-" * 40)
        
        # Generate random heights between 1 and 1000
        heights = [random.randint(1, 1000) for _ in range(size)]
        
        results = {}
        times = {}
        
        for name, func in implementations:
            # Skip brute force for large inputs
            if "Brute Force" in name and size > 500:
                print(f"{name:20}: Skipped (too slow)")
                continue
            
            # Warm up
            for _ in range(5):
                func(heights.copy())
            
            # Measure performance
            start_time = time.perf_counter()
            iterations = 1000 if size <= 100 else 100 if size <= 500 else 10
            
            for _ in range(iterations):
                result = func(heights.copy())
            
            end_time = time.perf_counter()
            avg_time = (end_time - start_time) / iterations
            
            results[name] = result
            times[name] = avg_time
            
            print(f"{name:20}: {avg_time*1000:.3f} ms/call -> area: {result}")
        
        # Calculate speedup
        if len(times) >= 2:
            brute_force_time = next((t for n, t in times.items() if "Brute Force" in n), None)
            optimal_time = next((t for n, t in times.items() if "Optimal" in n), None)
            
            if brute_force_time and optimal_time:
                speedup = brute_force_time / optimal_time
                print(f"\nSpeedup: {speedup:.1f}x faster with optimal solution")


def complexity_analysis():
    """Analyze and explain the complexity of different approaches."""
    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    
    print("""
🔍 PROBLEM: Container With Most Water
Given heights array, find two lines that form container holding most water.

📊 COMPLEXITY COMPARISON:

1️⃣ BRUTE FORCE APPROACH:
   • Time Complexity: O(n²)
   • Space Complexity: O(1)
   • Method: Check all possible pairs (i,j) where i < j
   • Pros: Simple to understand and implement
   • Cons: Inefficient for large inputs

2️⃣ OPTIMAL TWO-POINTER APPROACH:
   • Time Complexity: O(n) ⭐
   • Space Complexity: O(1) ⭐
   • Method: Start from both ends, move pointer with smaller height
   • Pros: Optimal time and space complexity
   • Cons: Requires understanding of the greedy principle

🧠 WHY TWO-POINTER WORKS:
   • Key insight: Moving the taller pointer can only decrease area
   • Moving shorter pointer might find a taller line
   • We explore all potentially optimal solutions efficiently

🎯 OPTIMALITY PROOF:
   • At each step, we eliminate suboptimal solutions
   • The pointer movement ensures we don't miss the optimal solution
   • Mathematical proof: If we have heights[i] < heights[j], 
     any container using i with k (where i < k < j) will have:
     - Width: (k - i) < (j - i)
     - Height: min(heights[i], heights[k]) ≤ heights[i]
     - Therefore: area ≤ heights[i] × (k - i) < heights[i] × (j - i)

✅ CONCLUSION: The two-pointer solution IS OPTIMAL
   • Cannot be improved further in terms of time complexity
   • Uses minimal space
   • Handles all edge cases correctly
""")


def visual_example():
    """Provide a visual example of how the algorithm works."""
    print("\n" + "=" * 60)
    print("VISUAL EXAMPLE")
    print("=" * 60)
    
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Heights: {heights}")
    print("Indices: " + " ".join(f"{i}" for i in range(len(heights))))
    
    # Visualize the heights
    max_height = max(heights)
    print("\nVisualization:")
    for level in range(max_height, 0, -1):
        line = ""
        for h in heights:
            line += "█" if h >= level else " "
        print(f"{level:2d} |{line}|")
    
    print("   +" + "-" * len(heights) + "+")
    print("    " + "".join(str(i) for i in range(len(heights))))
    
    # Trace through the algorithm
    print(f"\nAlgorithm trace:")
    left, right = 0, len(heights) - 1
    max_area = 0
    step = 1
    
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        max_area = max(max_area, area)
        
        print(f"Step {step}: left={left}(h={heights[left]}), right={right}(h={heights[right]})")
        print(f"         width={width}, height={height}, area={area}, max_so_far={max_area}")
        
        if heights[left] < heights[right]:
            left += 1
            print(f"         Move left pointer (smaller height)")
        else:
            right -= 1
            print(f"         Move right pointer (smaller height)")
        
        step += 1
        if step > 10:  # Prevent too much output
            break
    
    print(f"\nFinal answer: {max_area}")


if __name__ == '__main__':
    # Original test
    print("Original test case:")
    result = largest_container([2, 7, 8, 3, 7, 6])
    print(f"largest_container([2, 7, 8, 3, 7, 6]) = {result}")
    
    # Comprehensive testing
    test_implementations()
    performance_comparison()
    complexity_analysis()
    visual_example()