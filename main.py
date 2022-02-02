import time

tests = {
    "test1": {
        "inputs": {
            "cards": [9, 7, 5, 4, 1],   # queried number is first number.
            "queried_number": 9},
        "output": 0},
    "test2": {
        "inputs": {
            "cards": [],    # cards is empty list.
            "queried_number": 3},
        "output": -1},
    "test3": {
        "inputs": {
            "cards": [-1, -3, -3, -3, -7, -9],  # cards duplicate.
            "queried_number": -3},
        "output": 1},
    "test4": {
        "inputs": {
             "cards": [10, -3, -7, -9],  # queried number is last number
             "queried_number": -9},
        "output": 3},
    "test5": {
        "inputs": {
            "cards": [6, 6, -10, -12],  # queried number is not in cards
            "queried_number": 3},
        "output": -1},
    "test6": {
        "inputs": {
            "cards": [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
            "queried_number": 95},
        "output": 5},
    "test7": {
        "inputs": {
            "cards": [100],  # only one card
            "queried_number": 100},
        "output": 0},
    "test8": {
        "inputs": {
            "cards": [10, 8, 6, 6, -1],
            "queried_number": -1},
        "output": 4
    }
}


# brute force solution
def locating_card_brute(cards: list, queried_number: int):
    if cards:
        position = 0
        while position < len(cards):
            if cards[position] == queried_number:
                return position
            position += 1
        else:
            return -1
    else:
        return -1


def tester(func):
    failed_test = []
    for test_number, test in tests.items():
        if func(**test["inputs"]) == test["output"]:
            continue
        else:
            failed_test.append(test_number)
    print(failed_test)


def chrono(func):
    a = time.time()
    for _ in range(1000000):
        for test in tests.values():
            func(**test["inputs"])
    b = time.time()
    chrono = b-a
    print(chrono)


#tester(queried_numbering_card_brute)
#chrono(queried_numbering_card_brute)  # 3.35 secs for 1 000 000 try


def better_solution(cards: list, queried_number: int):
    if cards:
        mid = len(cards)//2
        for _ in range(len(cards)):
            if cards[mid] == queried_number:
                return mid
            elif cards[mid] > queried_number:
                mid += 1
            elif cards[mid] < queried_number:
                mid -= 1
        return -1
    else:
        return -1


#chrono(locating_card_brute)  # 4.79 sec for 1 000 000 try

"""Although the above solution takes advantage of the fact that the cards are 
 sorted in decreasing order, it is slightly slower than the brute force 
 solution. How come ? 1. It takes advantage of this fact only once. 2.
 If the queried number isn't in the cards, some unnecessary operations will
  take place."""


def leverage_order(cards: list, queried_number: int):
    mid = len(cards)//2
    if cards[mid] == queried_number:
        return mid
    elif cards[mid] > queried_number:
        return "right", mid
    else:
        return "left", mid

def recursion_binary_search(cards: list, queried_number: int):
    if cards:
        search = leverage_order(cards, queried_number)
        print(search)
        if type(search) != int:
            if search[0] == "right":
                mid = search[1]
                leverage_order(cards[mid:], queried_number)
            elif search[0] == "left":
                mid = search[1]
                leverage_order(cards[:mid], queried_number)
            else:
                raise ValueError("we don't know what went wrong")
        else:
            return search
    else:
        return -1

"""
The above needs to be completed when I understand recursion, if possible 
"""


def binary_search(cards: list, queried_number: int):
    lo, hi = 0, len(cards)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        if cards[mid] == queried_number:
            return mid
        elif cards[mid] > queried_number:
            lo = mid + 1
        elif cards[mid] < queried_number:
            hi = mid - 1
    return -1


#tester(binary_search)
#chrono(binary_search)   # 3.6 sec for 1 000 000 try

"""
the above could be tweaked so if there are duplicate I can choose which one 
the duplicate, based on position, should be returned.
"""


def tweaked_binary_search(cards: list, queried_number: int, checker: int = None):
    result = binary_search(cards, queried_number)
    if cards[result - 1] == queried_number:
        pass


tester(tweaked_binary_search)
