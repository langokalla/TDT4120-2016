from sys import stdin


class Node:
    def __init__(self):
        self.barn = {}      #Nodebarn av Node
        self.posi = []      #Indekser med ordstart


def main():
    ordliste = stdin.readline().split()
    sok = stdin.read()
    ordbok = {}
    pos = 0

    if '?' in sok:
        for ord in ordliste:
            if ord not in ordbok:
                toppNode = Node()
                for bokstav in ord:
                    if bokstav not in toppNode.barn:
                        toppNode.barn[bokstav] = Node()
                    toppNode = toppNode.barn[bokstav]
                ordbok[ord] = toppNode.posi
            ordbok[ord].append(pos)
            pos += len(ord) + 1
    else:
        for ord in ordliste:
            if ord not in ordbok:
                ordbok[ord] = []
            ordbok[ord].append(pos)
            pos += len(ord) + 1

    for ord in sok.split():
        if ord in ordbok:
            posi = ordbok[ord]
        elif '?' in ord:
            'hallo'
            noder = [Node()]
            for bokstav in ord:
                nye = []
                for node in noder:
                    if bokstav == '?':
                        nye.extend(node.barn.values())
                    elif bokstav in node.barn:
                        nye.append(node.barn[bokstav])
                noder = nye
            posi = []
            for node in noder:
                posi.extend(node.posi)
            ordbok[ord] = posi
        else:
            'hei'
            posi = []
            ordbok[ord] = posi
        posi.sort()
        print("%s: " % ord, end='')
        for p in posi:
            print(" %s" % p, end='')
        print()


"""def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)
"""

if __name__ == "__main__":
    main()
