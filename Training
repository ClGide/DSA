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
