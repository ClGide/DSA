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
