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
    },
    "test9": {
        "inputs": {
            "cards": [12, 10, 9, 7, 6, 6, 6, 6, 4, 3, 3, 3, 1],
            "queried_number": 6},
        "output": 4
    },
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


def tester(func, tests):
    failed_test = []
    for test_number, test in tests.items():
        if func(**test["inputs"]) == test["output"]:
            continue
        else:
            failed_test.append(test_number)
    print(failed_test)

#tester(queried_numbering_card_brute)

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


def test_location(cards, queried_number, mid):
    mid_number = cards[mid]
    if mid_number == queried_number:
        if mid-1 >= 0 and cards[mid-1] == queried_number:
            return "left"
        else:
            return "found"
    elif mid_number > queried_number:
        return "right"
    else:
        return "left"


def binary_search(cards: list, queried_number: int):
    lo, hi = 0, len(cards)-1

    while lo <= hi:  # if cards is empty, hi = -1 & the cond isn't fulfilled.
        mid = (lo + hi) // 2
        result = test_location(cards, queried_number, mid)
        #print(f"lo: {lo}, hi:{hi}, mid:{mid}, mid_number:{cards[mid]}")
        if result == "found":
            print(mid)
            return mid
        elif result == "right":
            lo = mid + 1
        elif result == "left":
            hi = mid - 1
    return -1


#tester(binary_search, tests)


"""
the above could be tweaked (I think) so if there are duplicate I can
choose which one of the duplicate, based on position, should be returned.
"""


def tweaked_binary_search(cards: list, queried_number: int, checking: int = None):
    result = binary_search(cards, queried_number)
    if cards[result - 1] == queried_number:
        pass


#tester(tweaked_binary_search, tests)


"""
Given an array of numbers in increasing order and a queried number, return the start 
index and the end index.
"""


tests_two = {
    "test1": {
        "inputs": {
            "cards": [10, 10, 10, 12, 13, 15],   # query is first number.
            "queried_number": 10},
        "outputs": (0, 2)},
    "test2": {
        "inputs": {
            "cards": [],    # cards is empty list.
            "queried_number": 3},
        "outputs": -1},
    "test3": {
        "inputs": {
            "cards": [1, 3, 3, 3, 7, 9, 9, 9, 9],  # query is last number.
            "queried_number": 9},
        "outputs": (5, 8)},
    "test4": {
        "inputs": {
            "cards": [1, 3, 3, 3, 7, 9, 9, 10, 13],  # query is repeated once.
            "queried_number": 7},
        "outputs": (4, 4)},
}


def left_right(mid_number, queried_number):
    if mid_number > queried_number:
        return "left"
    else:
        return "right"


def locate_first(cards, queried_number, mid):
    mid_number = cards[mid]
    if mid_number == queried_number:
        if mid-1 >= 0 and cards[mid-1] == queried_number:
            return "left"
        else:
            return "found"
    else:
        direction = left_right(mid_number, queried_number)
        return direction


def locate_last(cards, queried_number, mid):
    mid_number = cards[mid]
    last_index = len(cards)-1
    if mid_number == queried_number:
        if mid + 1 <= last_index and cards[mid + 1] == queried_number:
            return "right"
        else:
            return "found"
    else:
        direction = left_right(mid_number, queried_number)
        return direction


def return_first(cards, queried_number):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        result = locate_first(cards, queried_number, mid)
        if result == "left":
            hi = mid-1
        elif result == "right":
            lo = mid+1
        else:
            first = mid
            break
    return first


def return_last(cards, queried_number):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        result = locate_last(cards, queried_number, mid)
        if result == "left":
            hi = mid-1
        elif result == "right":
            lo = mid+1
        else:
            last = mid
            break
    return last


def locate_first_last(cards, queried_number):
    if not cards:
        return -1
    first = return_first(cards, queried_number)
    last = return_last(cards, queried_number)
    return first, last


locate_first_last(**tests_two["test4"]["inputs"])

#tester(locate_first_last, tests_two)

