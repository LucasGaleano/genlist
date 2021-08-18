from rule import rules
from itertools import combinations, chain


maxlevel = 1
words = ['lucas','test']
word = 'lucas'

map_leet = {'a':'4','e':'3','i':'1','o':'0', 's':'$','l':'1'}

def all_subset(iterable):
    return  list(chain.from_iterable(combinations(iterable, r) for r in range(1,len(iterable)+1)))

leet = []
for i, letter in enumerate(word):
    if letter in list(map_leet.keys()):
        leet.append(i)

for comb in all_subset(leet):
    aux = list(word)
    for i in comb:
        aux[i] = map_leet[aux[i]]
    print(''.join(aux))
