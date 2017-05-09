from sys import stdin
from itertools import repeat


def merge(decks):
    while len(decks) > 1:  # sorterer listene i merge-lignende stil
        liste1 = decks.pop(0)
        liste2 = decks.pop(0)
        listami = []

        while len(liste1) > 0 and len(liste2) > 0:
            if liste1[0] < liste2[0]:
                listami.append(liste1.pop(0))
            else:
                listami.append(liste2.pop(0))
        listami.extend(liste1)
        listami.extend(liste2)
        decks.append(listami)
        bokstavliste = []
    for (tall, bokstav) in decks[0]:
        bokstavliste.append(bokstav)
    return ''.join(bokstavliste)


def main():
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    print(merge(decks))


if __name__ == "__main__":
    main()