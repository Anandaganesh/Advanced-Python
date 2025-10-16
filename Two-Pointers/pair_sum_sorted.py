def pair_sum_sorted(lst, sum):
    if len(lst) > 1:
        i = 0
        j = len(lst) - 1

        while i < j:
            if lst[i] + lst[j] < sum:
                i+=1
            elif lst[i] + lst[j] > sum:
                j-=1
            else:
                return [i, j]
    return []


if __name__ == "__main__":
    print(pair_sum_sorted([-5, -2, 3, 4, 6], 7))

"""
Algorithmic Complexity Analysis
Your pair sum program has the following complexity characteristics:

Time Complexity: O(n)
The algorithm uses two pointers (i and j) that start at opposite ends of the array
In each iteration, exactly one pointer moves (either i increments or j decrements)
In the worst case, the pointers will meet in the middle, meaning we traverse the array at most once
Each comparison and pointer movement is O(1) operation
Therefore, the overall time complexity is O(n) where n is the length of the array
Space Complexity: O(1)
The algorithm uses only a constant amount of extra space
Variables i, j are the only additional storage used
No additional data structures are created
The space usage doesn't grow with input size
Therefore, the space complexity is O(1) - constant space

Why This is Optimal
This is actually an optimal solution for the sorted array pair sum problem because:

Time Efficiency: O(n) is the best possible time complexity for this problem since you need to examine the data at least once to find the answer.

Space Efficiency: O(1) space is optimal as you don't need any additional storage proportional to input size.

Two-Pointer Technique: This approach leverages the sorted property of the array effectively, avoiding the need for nested loops (which would be O(n²)) or hash tables (which would require O(n) extra space).
"""