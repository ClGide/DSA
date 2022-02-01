import time

tests = {
    "test1": {
        "inputs": {
            "cards": [9, 7, 5, 4, 1],
            "pick": 9},
        "output": 0},
    "test2": {
        "inputs": {
            "cards": [],
            "pick": 3},
        "output": None},
    "test3": {
        "inputs": {
            "cards": [-1, -3, -3, -3, -7, -9],
            "pick": -3},
        "output": 1},
    "test4": {
        "inputs": {
             "cards": [10, -3, -7, -9],
             "pick": -9},
        "output": 3},
    "test5": {
        "inputs": {
            "cards": [6, 6, -10, -12],
            "pick": 3},
        "output": None},
    "test6": {
        "inputs": {
            "cards": [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
            "pick": 95},
        "output": 5},
}


# brute force solution
def picking_card_brute(cards: list, pick: int):
    if cards:
        for card in cards:
            if card == pick:
                return cards.index(card)
    else:
        return None


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


tester(picking_card_brute)
chrono(picking_card_brute)  # 2.4 secs for 1 000 000 try

