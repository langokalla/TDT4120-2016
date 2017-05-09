l = [1,2,3,4,5,6,7,8,9]
del l[7]
print(l[int(len(l)/2):])

print('\n\n')

decks = [[(1, 'o'), (6, 'o')], [(2, 'm'), (7, 'm')]]
s1 = decks.pop(0)
s2 = decks.pop(0)
print('s1:')
print(s1[0])
