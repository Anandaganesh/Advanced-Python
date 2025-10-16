def pair_sum_sorted(lst, sum):
    if len(lst) >= 2:
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