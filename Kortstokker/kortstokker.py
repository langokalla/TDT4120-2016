from sys import stdin
from itertools import repeat


def merge(decks):
    while len(decks) > 1:
        s1 = decks.pop(0)
        s2 = decks.pop(0)
        s = []
        while len(s1) > 0 and len(s2) > 0:
            if s1[0] < s2[0]:
                s.append(s1.pop(0))
            else:
                s.append(s2.pop(0))
        s.extend(s1)
        s.extend(s2)
        decks.append(s)
    letters = ''
    for (number, letter) in decks[0]:
        letters += letter
    return letters


def main():
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
        print(deck)
    print(merge(decks))


if __name__ == "__main__":
    main()
