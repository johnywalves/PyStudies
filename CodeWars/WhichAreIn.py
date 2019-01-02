"""
Which Are In

Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.

Beware: r must be without duplicates.
Don't mutate the inputs.
"""

def in_array(a1, a2):
    return sorted({w for w in a1 if w in "".join(a2)})

	
def in_array(a1, a2):
    return sorted({w for w in a1 if w in "".join(a2)})

	
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})


in_array = lambda array1, array2: sorted([x for x, y in dict(zip(array1, [len([w for b in array2 if w in b]) for w in array1])).items() if y != 0])


def in_array(array1, array2):
    lst = dict(zip(array1, [len([w for b in array2 if w in b]) for w in array1]))
    return sorted([x for x, y in lst.items() if y != 0])

	
def in_array(array1, array2):
    lst = dict()
    for w in array1:
        lst[w] = len([w for b in array2 if w in b])
    return sorted([x for x, y in lst.items() if y != 0])

	
def in_array(array1, array2):
    lst = dict()
    for w in array1:
        c = 0
        for b in array2:
            if w in b:
                c = c + 1
        lst[w] = c

    r = []
    for x, y in lst.items():
        if y != 0:
            r.append(x)
    r = sorted(r)
    return r