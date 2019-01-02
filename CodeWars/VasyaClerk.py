"""
Vasya Clerk

The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?
Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.
"""

tickets = lambda s: "NO" if sum(i * 25 < p - 25 for i, p in enumerate(s)) else "YES"


def tickets(people):
    return "NO" if sum(i * 25 < p - 25 for i, p in enumerate(people)) else "YES"	

	
def tickets(people):
    for i, p in enumerate(people):
        if i * 25 < p - 25:
            return "NO"
    return "YES"	

	
def tickets(people):
    c = 0
    for p in people:
        c += 1
        if ((c * 25) < (p - 25)):
            return "NO"
    return "YES"