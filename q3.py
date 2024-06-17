import itertools
import statistics

def mean(lst):
    return sum(lst) / len(lst)

def max_val(n, arr):
    ans = float('-inf')
    for c in range(1, n + 1):
        for subset in itertools.combinations(arr, c):
            subset_mean = mean(subset)
            subset_median = statistics.median(subset)
            val = subset_mean - subset_median
            if val > ans:
                ans = val
    return ans
