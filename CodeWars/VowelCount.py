"""
Vowel Count

Return the number (count) of vowels in the given string.
We will consider a, e, i, o, and u as vowels for this Kata.
The input string will only consist of lower case letters and/or spaces.
"""

getCount lambda i: len([l for l in i if l in 'aeiou'])


def getCount(input):
    return len(list(filter(lambda x: x in 'aeiou', input)))

	
getCount lambda i: len(list(filter(lambda x: x in 'aeiou', i)))


def getCount(inputStr):
    return len([x for x in inputStr if x in 'aeoiu'])

	
getCount = lambda s: sum(s.count(i) for i in 'aeiou')	


getCount = lambda iS:sum([1 for i in iS if i in "aeiou"])


getCount = lambda s: sum(e in "aiueo" for e in s)