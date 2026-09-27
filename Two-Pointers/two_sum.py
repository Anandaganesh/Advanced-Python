def two_sum(nums:list[int], target:int) -> list[int]:
    nums.sort()
    i = 0
    j = len(nums) - 1

    while i < j:
        current_sum = nums[i] + nums [j]
        
        if current_sum == target:
            return [nums[i], nums[j]]
        
        elif current_sum > target:
            j-=1
        else:
            i+=1
    return []


if __name__ == '__main__':
    print(two_sum([2, 5, 7, 15], 12))