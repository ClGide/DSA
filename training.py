""" problem nr1 """

"""
If the string is a valid variable name, return "good variable name". Otherwise, return
"bad variable name" + first character making it a bad variable name.
1. alphanumeric values and _ are accepted.
2. numbers cannot be used as the first character.
3. cannot be a keyword
"""

from keyword import iskeyword

a = "aaaè_ç"
b = "1feggfe"
c = "tarTE"
d = "_ejef"
e = "fefeg_e_"
f = "cfezv ee"
g = "cefez-fzfz"
h = "dsvess@?!/"
i = "a"

def func(s: str) -> str:
    if s.isidentifier() and not iskeyword(s):
        return "good variable name"
    else:
        if s[0].isdigit():
            err = s[0]
        else:
            err = next(filter(lambda x: not x.isalnum() or x in '_', s), None)
        return f"bad variable name:{err}"


tests = [a, b, c, d, e, f, g, h, i]
for test in tests:
    result = func(test)
    print(result)


""" problem nr2 """
    
    
from typing import List, Tuple, Dict

""" I need to solve the following algebraic equations"""

basic = "a + 1"
only_constants = "a + b - c + d + e" # only constants
harder = "3a - 7 + 2 - 6d + 3c"  # odd 
harder_bis = "3b + 2 + 4 - 9"  # even
constants = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", -3)]


"""
I want to do something akin to the reduce built-in function.  
I replace the first three items in the list with a value, and 
I repeat the  process. The value is the result of the computation. The process 
ends when there's only one value left in the list. 
I'll use a helper function. It'll replace all the values corresponding to a constant 
with the result of the multiplication.  
"""

def multiplication(num: List[str], const_value: Dict[str, int]) -> List[str]:
    for idx, val in enumerate(num):
        if len(val) > 1:
            num[idx] = const_value[val[1]] * int(val[0])
        elif val.isalpha():
            num[idx] = const_value[val]
    return num

def algebraic_computation(num: str, constants: List[Tuple[str, int]]) -> int:
    const_value = {k:v for k, v in constants}
    nums_to_add_subtract_multiply = num.split(" ")
    nums_to_add_subtract = multiplication(nums_to_add_subtract_multiply, const_value)
    n = nums_to_add_subtract
    first_n, operator, sec_n = 0, 1, 2
    
    # this is a risky operation as I am modifying the list I am looping through
    while len(n) > 1:
        if n[operator] == "+":
            n[0] = int(n[first_n]) + int(n[sec_n])
            del n[1:3]
        elif n[operator] == "-":
            n[0] = int(n[first_n]) - int(n[sec_n])
            del n[1:3]
        else:
            raise ValueError("the values seems to be badly formatted.")
    return n[0]


""" problem nr3 """


test_1 = "AABCC"
test_2 = "In some ways, programming is like painting. You start with" \
         " a blank canvas and certain basic raw materials. You use a" \
         " combination of science, art, and craft to determine what to do with them."

"""
sol_test_1: 
* *
***
ABC

sol_test_2:
*
*
*
*
*
*       *        *
*       *        *
*       *   *    *
*       *   *    *
*   *   *   *    *
*   *   *   **   *
*   *   *   ** ***
*   *   *   ** ***
* * *   *  *** ***
* * *   *  *** ***
* * *   *  *** ***  *
* ***  **  *** ***  *
***** *** **** **** **
******************* **
**********************
ABCDEFGHIKLMNOPRSTUVWY
"""


def painting(words:str) -> str:
    ch_indexes = {}
    for idx, ch in enumerate(words):
        if ch not in ch_indexes:
            ch_indexes[ch] = 1
        else:
            ch_indexes[ch] += 1

    ch_upper_indexes = {
        key.upper():value 
        for key, value 
        in ch_indexes.items() if key.isalpha()
    }
    ch_upper_indexes_sorted = {
        key:value 
        for key, value 
        in zip(sorted(list(ch_upper_indexes.keys())), ch_upper_indexes.values())
    }

    r = ""
    for height in range(max(ch_upper_indexes_sorted.values()), 0, -1):
        for letter in ch_upper_indexes_sorted.keys():
                if ch_upper_indexes_sorted[letter] >= height:
                    r += "*"
                else:
                    r += " "
                if letter == sorted(ch_upper_indexes_sorted.keys())[-1]:
                    r += "\n"
    r += "".join(ch_upper_indexes_sorted.keys())
    
    return r 





""""problem nr3 - JumpGame - work in progress"""""

"""
That's a fun one.
1. State the problem clearly. Identify the inputs and outputs format.
The input is a list of integers named nums. There can be no empty list. There can be as many as 10^4 integers.
The output is a boolean.
We need to return True if we can reach the last index. We start from the first index. Its value is the maximum jump we
can do. In other words, we can move forward up to that value. If the maximum jump is 3, we can move forward 3, 2 or 1.
2. Write some tests. Think of some edge cases.
"""

test1 = ([0, 0, 0, 0, 0], False)
test2 = ([0], True)
test3 = ([4], True)
test4 = ([3, 2, 0, 1, 1], True)
test5 = ([3, 2, 1, 0, 4], False)
test6 = ([2, 3, 1, 1, 4], True)
test7 = ([2, 0], True)
test8 = ([2, 0, 0], True)
tests = [test7, test6, test5, test4, test3, test2, test1]

"""
3. Think of some solution, state it in plain english.
There are two ways we can end the loop. Either the counter is equal to the sum of numbers in nums (and we return False), either 
we get to the end of nums (and we return True). Getting to the end of nums is the same as having a sum equal or
superior to the length of nums minus one. The counter is increased at every new trial. 
We need a dictionary. The keys are indexes in nums. The value is a list of used values of those indexes. There must never be more 
than two lists in the dict whose last item is one.  
At each trial we check in the dictionary if there's a key with last_updated_index. If there isn't, we create one and the value
is a list with one item, the value of the last_updated_index. If there is a key with the last_updated_index, we check the last value in 
its list. If the last value is 1, we add 1 to last_updated_index and create a new key value pair in the dict. If the last value is  not
1, we add this last value - 1 at the end of the list and start a new trial with that value. 
Now, when there's more than one key in the dictionary, we still need to start the trial at the first index. In other words, we need to 
keep track during the trial of multiple values.  
To make a trial, we get the value (v1) of the first index (i1), and add it to the value located at index v1. And so on until 
the value we get to is zero OR the sum is equal or superior to the length of the list OR the counter is equal to the sum 
of numbers inside the list. In the first case, we get back to the first index and start again. The important thing is that
each time we select a value in the list we decrease it by one.    
"""


def brute_force_check_function(func: callable, tests: [tuple[list, bool]]) -> list[bool]:
    results = []
    for test in tests:
        if func(test[0]) == test[1]:
            results.append(True)
        else:
            results.append(False)
    return results


def brute_force(nums: list[int]) -> bool:
    index_used_values: dict[int, list[int]] = {}
    nr_of_trials = 0
    max_nr_of_trials = sum(nums)
    last_updated_index = 0
    target = len(nums) - 1
    while nr_of_trials <= max_nr_of_trials:
        if last_updated_index not in index_used_values.keys():
            index_used_values[last_updated_index] = [nums[last_updated_index]]
        else:
            last_used_value = index_used_values[last_updated_index][-1]
            if last_used_value == 1:
                last_updated_index = last_updated_index + 1
                index_used_values[last_updated_index] = [nums[last_updated_index]]
            elif last_used_value > 1:
                index_used_values[last_updated_index].append(last_used_value - 1)
        i = 0
        jumps = 0
        if target == jumps:  # for the special case where nums is [0]
            return True
        while True:
            if i in range(len(nums)):
                if nums[i] == 0:
                    break
            if jumps >= target:
                return True
            if i in index_used_values.keys():
                value_to_use = index_used_values[i][-1]
            else:
                value_to_use = nums[i]
            jumps += value_to_use
            i += value_to_use
        nr_of_trials += 1
    return False


result = brute_force_check_function(brute_force, tests)
print(result)
