"""
Friends or Foe

Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
Note: keep the original order of the names in the output.
"""

friend = lambda x: [n for n in x if len(n) == 4]


def friend(x):
    y = x.copy()
    for n in y:
        if len(n) != 4:
            x.remove(n)
    return x

	
def friend(x):
    return list(filter(lambda s : len(s)==4 ,x))

	
def friend(x):
    return [y for y in x if len(y)==4]

	
def friend(x):
    return [f for f in x if len(f) == 4]	