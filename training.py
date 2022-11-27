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






"""problem nr3 GroupAnagrams"""

"""
1. State the problem clearly. Identify the inputs and the outputs format.
A list of strings is going to be given to me. I need to identify groups of anagrams.
In other words, I have to identify which strings are of the same length and are composed
of exactly the same characters, even if the order is different. I have to return those
groups of anagrams as a list of lists of strings.
2. Think of edge cases.
Some strings may be composed of the same characters but be of different length => different groups.
There may be a list with only one string => return that one string in its own list.
One or more strings may be of length 0 => return that or those strings in its/their own list.
There may be no anagrams in the list of strings => return the empty list.
3. Come up with a correct solution. State it in plain english.
The brute force solution would be to calculate for each string all possible anagrams.
If the possible anagram is in the list of strings, add it to the group. Remove the found
anagram from the list. After calculating all the possible anagrams of string i, start again from
string i+1. Strings that aren't part of any anagram should be appended to the result as singlets
at the end.
"""

import time


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#expected_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

strs_1 = [""]
strs_2 = ["a"]

"""
4. Implement the solution. Fix bugs, if any. 
So there is a IndexError when the input is composed of only two identical empty strings. 
The solution is to identify all identical strings at the beginning of the algorithm. The idea is to
remove them from the list of strings and to add them to their group. Only if the list of strings is
non empty after this operation, should we go on computing all possible anagrams of each remaining string.
 
Let's make a function that groups identical strings in their own groups and removes them from the
original list. This function's input is a list of strings. This function has two outputs, the list 
of remaining strings (can be an empty list) and the list of lists of identical strings(can be empty as well). 
"""

test_1 = ["", ""]
test_2 = ["cca", "cac", "bb", 'cac', "b", "cac", "bb"]  # cac repeated thrice, bb repeated twice
test_3 = ["cac", "dac", "bab", 'c', "b", "clc", "pbb"]  # no repeating strings


"""
5. Identify inefficiencies, if any. Think of some improvements. 
Given the test case that is making us fail, the problem is that 
itertools.permutations considers all items in a sequence unique based
on their position (which can create a lot of useless identical anagrams). So, 
I found a function on stack overflow that returns all permutations
of a sequence considering items unique based on value.
"""

speed_test_1 = ["bdddddddddd", "bbbbbbbbbbc"]

"""
4. Fix bugs, if any. 
After we identified the repeating characters there's some weird behavior inside the loop.
At the first iteration it creates possible anagrams with the first element. 
At the second iteration it creates possible anagrams with the second element in the list instead of taking the first one. 
Which isn't that weird because the counter passed from 0 to 1 and the first element from the original list of strings has 
been removed. 
The consequence is that the loop doesn't compute the anagrams for all strings. The reason that the algorithm worked for
all test cases until now is that taking computing anagrams for one of two strings was enough to return 
the correct output (either the strings for which possible anagrams weren't computed didn't have anagrams in the list OR did
have anagrams for which possible anagrams were computed). 
There are two possible solutions. First, we can restart the loop if when it ends the original list of strs isn't empty. Second, 
we can replace the for loop with a while loop in order to always compute anagrams of the first element in the original list 
until the list is empty. The second option seems the cleanest.  
"""

test_4 = ["abets", "bead", "remain", "betas", "abed", "baste", "airline", "leading", "beast", "dealing", "beats", "airmen", "marine", "single", "bade", "aligned"]
test_5 = ["", "b"]
test_6 = ["and", "dan"]


"""
4. Fix bugs, if any. 
Our algorithm with fail when the test case contains a repeated string which also have anagram(s) in the 
input. Indeed, our algorithm comprise two separate steps. The first step separates identical strings from 
the rest of the input. The second step finds anagrams for the remaining strings. The reason for this two-step
approach is an IndexError when we were using a for loop. However, now that we are using a while loop, we may try
to eliminate the preliminary step. 
"""

test_7 = ["tea", "", "eat", "", "tea", ""]


class Solution:
    def unique_permutations(self, elements):
        if len(elements) == 1:
            yield elements[0]
        else:
            unique_elements = set(elements)
            for first_element in unique_elements:
                remaining_elements = list(elements)
                remaining_elements.remove(first_element)
                for sub_permutation in self.unique_permutations(remaining_elements):
                    yield first_element + sub_permutation

    def groupAnagrams(self, strs):
        output = []
        n = len(strs)
        if n == 0:
            return output
        else:
            while n > 1:
                print(f"n:{n} \nstrs:{strs}, \noutput:{output}\n")
                group = []
                first_string = strs[0]
                if len(first_string) > 0:
                    for word in self.unique_permutations(first_string):
                        if word in strs:
                            print(f"word:{word}")
                            nr_identical_strs = strs.count(word)
                            if nr_identical_strs > 1:
                                for _ in range(nr_identical_strs):
                                    group.append(word)
                                    strs.remove(word)
                            else:
                                group.append(word)
                                strs.remove(word)
                if len(group) > 0:
                    output.append(group)
                if first_string in strs and len(first_string) == 0:
                    nr_identical_empty_strs = strs.count("")
                    output.append(nr_identical_empty_strs * [""])
                    for _ in range(nr_identical_empty_strs):
                        strs.remove("")
                n = len(strs)
            for left_string in strs:
                output.append([left_string])
            return output


"""
Our algorithm is still faulty. If one word's anagram is a repeating string located at a higher index
in the list, then the repeated strings will be splitted in two separate groups. 
Say we have ["AZ", "B", "ZA", "ZA"], at the first iteration our algorithm will add to the output the 
following group ["ZA", "AZ"] instead of ["ZA", "ZA", "AZ"]. The reason is that our algorithm doesn't check
if a word's anagram found in the list is repeated. It only checks if a word is repeated in a list
before computing its anagrams. 
Why did we decide to check for repeating strings before computing anagrams ? It doesn't seem to be a necessary
choice. Would our algorithm work with all test cases if it only checked for repeated strings of anagrams found 
in the list ? What would happen if a repeated string didn't have any anagram in the list ? Our algorithm would 
still work if the word "AZ" is considered an anagram of "AZ". Which is the case. 
"""

test_8 = ["rag", "orr", "err", "bad", "foe", "ivy", "tho", "gem","len","cat","ron","ump","nev","cam","pen","dis","rob","tex","sin","col","buy","say","big","wed","eco","bet","fog","buy","san","kid","lox","sen","ani","mac","eta","wis","pot","sid","dot","ham","gay","oar","sid","had","paw","sod","sop"]
#actual_output = [["rag"],["orr"],["err"],["bad"],["foe"],["ivy"],["tho"],["gem"],["len"],["cat"],["ron"],["ump"],["nev"],["cam","mac"],["pen"],["sid","dis"],["rob"],["tex"],["sin"],["col"],["buy","buy"],["say"],["big"],["wed"],["eco"],["bet"],["fog"],["san"],["kid"],["lox"],["sen"],["ani"],["eta"],["wis"],["pot"],["dot"],["ham"],["gay"],["oar"],["sid"],["had"],["paw"],["sod"],["sop"]]
#expected_output = [["sop"],["sod"],["paw"],["oar"],["dot"],["ani"],["sen"],["kid"],["nev"],["ump"],["rob"],["cam","mac"],["len"],["gem"],["eta"],["tex"],["gay"],["sin"],["cat"],["wis"],["eco"],["tho"],["had"],["foe"],["bad"],["rag"],["ivy"],["orr"],["bet"],["pen"],["dis","sid","sid"],["lox"],["ron"],["col"],["buy","buy"],["ham"],["err"],["say"],["big"],["pot"],["wed"],["fog"],["san"]]
# the error is that the algorithm returns "dis sid" and "sid" instead of "dis sid sid"


"""
5. Identify inefficiencies, if any. Think of some improvements. 
The question is what slows down the algorithm when facing a long list (567 items) ? Is it computing permutations for 
each word ? Is it the .count method applied to each of those anagram (which also implies some kind of looping through
the entire list) ? Is it looping again and again through the list ?
I wouldn't have thought that my brute force solution is SO inefficient. The time complexity of unique_permutations is
to be quadratic. Thus, before even thinking of further problems, we have to change unique_permutations. And I think that 
implies completely changing our algorithm. 
One preliminary thing we can do that doesn't directly solve our problem is changing our initial list into a dictionary where
the key is the length of the string and the value is a list of strings of that length.
Then, for each of those lists of strings, we try to create groups little by little. How ? 
"""

speed_test_2 = ["compilations", "bewailed", "horology", "lactated", "blindsided", "swoop", "foretasted", "ware", "abuts", "stepchild", "arriving","magnet","vacating","relegates","scale","melodically","proprietresses","parties","ambiguities","bootblacks","shipbuilders","umping","belittling","lefty","foremost","bifocals","moorish","temblors","edited","hint","serenest","rendezvousing","schoolmate","fertilizers","daiquiri","starr","federate","rectal","case","kielbasas","monogamous","inflectional","zapata","permitted","concessions","easters","communique","angelica","shepherdess","jaundiced","breaks","raspy","harpooned","innocence","craters","cajun","pueblos","housetop","traits","bluejacket","pete","snots","wagging","tangling","cheesecakes","constructing","balanchine","paralyzed","aftereffects","dotingly","definitions","renovations","surfboards","lifework","knacking","apprises","minimalism","skyrocketed","artworks","instrumentals","eardrums","hunching","codification","vainglory","clarendon","peters","weeknight","statistics","ay","aureomycin","lorrie","compassed","speccing","galen","concerto","rocky","derision","exonerate","sultrier","mastoids","repackage","cyclical","gowns","regionalism","supplementary","bierce","darby","memorize","songster","biplane","calibrates","decriminalizes","shack","idleness","confessions","snippy","barometer","earthing","sequence","hastiness","emitted","superintends","stockades","busywork","dvina","aggravated","furbelow","hashish","overextended","foreordain","lie","insurance","recollected","interpreted","congregate","ranks","juts","dampen","gaits","eroticism","neighborhoods","perihelion","simulations","fumigating","balkiest","semite","epicure","heavier","masterpiece","bettering","lizzie","wail","batsmen","unbolt","cudgeling","bungalow","behalves","refurnishes","pram","spoonerisms","cornered","rises","encroachments","gabon","cultivation","parsed","takeovers","stampeded","persia","devotional","doorbells","psalms","cains","copulated","archetypal","cursores","inbred","paradigmatic","thesauri","rose","stopcocks","weakness","ballsier","jagiellon","torches","hover","conservationists","brightening","dotted","rodgers","mandalay","overjoying","supervision","gonads","portage","crap","capers","posy","collateral","funny","garvey","ravenously","arias","kirghiz","elton","gambolled","highboy","kneecaps","southey","etymology","overeager","numbers","ebullience","unseemly","airbrushes","excruciating","gemstones","juiciest","muftis","shadowing","organically","plume","guppy","obscurely","clinker","confederacies","unhurried","monastic","witty","breastbones","ijsselmeer","dublin","linnaeus","dervish","bluefish","selectric","syllable","pogroms","pacesetters","anastasia","pandora","foci","bipartisan","loomed","emits","gracious","warfare","uncouples","augusts","portray","refinery","resonances","expediters","deputations","indubitably","richly","motivational","gringo","hubris","mislay","scad","lambastes","reemerged","wart","zirconium","linus","moussorgsky","swopped","sufferer","sputtered","tamed","merrimack","conglomerate","blaspheme","overcompensate","rheas","pares","ranted","prisoning","rumor","gabbles","lummox","lactated","unzipping","tirelessly","backdate","puzzling","interject","rejections","bust","centered","oxymoron","tangibles","sejong","not","tameness","consumings","prostrated","rowdyism","ardent","macabre","rustics","dodoes","warheads","wraths","bournemouth","staffers","retold","stiflings","petrifaction","larkspurs","crunching","clanks","briefest","clinches","attaching","extinguished","ryder","shiny","antiqued","gags","assessments","simulated","dialed","confesses","livelongs","dimensions","lodgings","cormorants","canaries","spineless","widening","chappaquiddick","blurry","lassa","vilyui","desertions","trinket","teamed","bidets","mods","lessors","impressiveness","subjugated","rumpuses","swamies","annotations","batiks","ratliff","waxwork","grander","junta","chutney","exalted","yawl","joke","vocational","diabetic","bullying","edit","losing","banns","doleful","precision","excreting","foals","smarten","soliciting","disturbance","soggily","gabrielle","margret","faded","pane","jerusalem","bedpan","overtaxed","brigs","honors","repackage","croissants","kirov","crummier","limeades","grandson","criers","bring","jaundicing","omnibusses","gawking","tonsillectomies","deodorizer","nosedove","commence","faulkner","adultery","shakedown","wigwag","wiper","compatible","ultra","adamant","distillation","gestates","semi","inmate","onlookers","grudgingly","recipe","chaise","dialectal","aphids","flimsier","orgasm","sobs","swellheaded","utilize","karenina","irreparably","preteen","mumble","gingersnaps","alumnus","chummiest","snobbish","crawlspaces","inappropriate","ought","continence","hydrogenate","eskimo","desolated","oceanic","evasive","sake","laziest","tramps","joyridden","acclimatized","riffraff","thanklessly","harmonizing","guinevere","demanded","capabler","syphilitics","brainteaser","creamers","upholds","stiflings","walt","luau","deafen","concretely","unhand","animations","map","limbos","tranquil","windbreakers","limoges","varying","declensions","signs","green","snowbelt","homosexual","hopping","residue","ransacked","emeritus","pathologist","brazenly","forbiddingly","alfredo","glummest","deciphered","delusive","repentant","complainants","beets","syntactics","vicissitude","incompetents","concur","canaan","rowdies","streamer","martinets","shapeliness","videodiscs","restfulness","rhea","consumed","pooching","disenfranchisement","impoverishes","behalf","unsuccessfully","complicity","ulcerating","derisive","jephthah","clearing","reputation","kansan","sledgehammer","benchmarks","escutcheon","portfolios","mandolins","marketable","megalomaniacs","kinking","bombarding","wimple","perishes","rukeyser","squatter","coddle","traditionalists","sifts","agglomerations","seasonings","brightness","spices","claimant","sofas","ambulatories","bothered","businessmen","orly","kinetic","contracted","grenadiers","flooding","dissolved","corroboration","mussed","squareness","alabamans","dandelions","labyrinthine","pot","waxwing","residential","pizza","overjoying","whelps","overlaying","elanor","tented","masterminded","balsamed","powerhouses","tramps","eisenstein","voile","repellents","beaus","coordinated","wreckers","eternities","untwists","estrangements","vitreous","embodied"]


def grouping_strings_by_len(strs: list[strs]) -> dict[int, strs]:
    strings_grouped_by_len = {}
    for word in strs:
        length = len(word)
        if length in strings_grouped_by_len:
            strings_grouped_by_len[length].append(word)
        else:
            strings_grouped_by_len[length] = [word]
    return strings_grouped_by_len


s = Solution()
mini_speed_test = ["compilations", "bewailed", "horology", "ompilationcs"]


class Solution_improved:
    def create_checksum(self, str):
        hashes = []
        for ch in str:
            hashes.append(hash(ch))
        return sum(hashes)

    def associate_str_checksum(self, strs):
        checksum_str = {}
        for str in strs:
            checksum = self.create_checksum(str)
            if checksum in checksum_str:
                checksum_str[checksum].append(str)
            else:
                checksum_str[checksum] = [str]
            groups = list(checksum_str.values())
        return groups






"""problem nr4 - JumpGame - work in progress"""

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
