tests = {
    "test1":
        {"input": [10, 12, 13, 15, 0, 1, 3, 5],
         "output": 4},
    "test2":
        {"input": [1],
         "output": 0},
    "test3":
        {"input": [11, 12, 15, 16, 18],
         "output": 0},
    "test4":
        {"input": [49, 1, 4, 9, 10, 12],
         "output": 5},
    "test5":
        {"input": [],
         "output": -1},
    "test1_rep":
        {"input": [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4],
         "output": 6},
    "test2_rep":
        {"input": [5, 6, 6, 9, 9, 9, 9, 9, 3, 3, 3, 3, 3, 4, 4],
         "output": 8},
    "test1_target":
        {"input": ([11, 12, 13, 18, 1, 2, 3], 12),
         "output": 4},
    "test2_target":
        {"input": ([11, 12, 13, 1, 2, 3, 5, 7, 8, 9], 11),
         "output": 7},
    "test3_target":
        {"input": ([11, 12, 13, 18, 1, 2, 3], 10),  # target not in list.
         "output": -1},
    "test4_target":
        {"input": ([], 10),  # nums is empty.
         "output": -1},
    "test5_target":
        {"input": ([11, 14, 18, 20, 22, 26, 30], 30),  # nums wasn't rotated.
         "output": 6},
    "test6_target":
        {"input": ([37, 39, 45, 12, 18, 30], 30),  # num is the last number.
         "output": 2},


}


def brute_force(nums):
    if not nums:
        return -1
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            return i
    return 0


res = brute_force(tests["test4"]["input"])
#print(res)


def binary_search(nums):
    lo, hi = 0, len(nums)-1
    if len(nums) == 1:
        return 0

    while lo <= hi:
        mid = (lo + hi) // 2
        before_mid = mid-1

        if nums[before_mid] > nums[mid]:
            return check_for_repetition(nums, mid, before_mid)
        elif nums[mid] <= nums[hi]:
            hi = mid - 1
        elif nums[mid] >= nums[hi]:
            lo = mid + 1

    return -1


def check_for_repetition(nums, mid, before_mid):
    while before_mid >= 0:
        if nums[before_mid] != nums[mid]:
            return mid
        else:
            before_mid -= 1
            mid -= 1


res = binary_search(tests["test2_rep"]["input"])
print(res)


def brute_force_target(nums, target):
    if not nums:
        return -1

    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            break
    count = 0
    while count < len(nums):
        i = (i + 1) % len(nums)
        count += 1
        if nums[i] == target:
            return count
    return -1


res = brute_force_target(*tests["test6_target"]["input"])


"""
the problem is that w/ test_five, count is getting increased
before it should.

def understanding_why_test_five_isnt_passing():
    for i in range(10):
        print(i)
        if i == 7:
            break
    count = 2
    print(count)

f()
"""