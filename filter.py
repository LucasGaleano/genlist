from itertools import combinations, chain
from functools import reduce


class Prefilter():

    @classmethod
    def nothing(cls, word):
        return word

    @classmethod
    def capital_first(cls, word):
        return word.capitalize()
   
    @classmethod
    def apply_all_filters(cls, word):
        fword = word
        aux = set()
        iterable = [cls.nothing, cls.capital_first]
        filters = powerset(iterable)
        for filt in filters:
            fword = word
            for f in filt:
                fword = f(fword)
            aux.add(fword)
        return aux




class Postfilter():
 
    
    @classmethod
    def nothing(cls, word):
        return word

    @classmethod
    def between_parenthesis(cls, word):
        return "("+word+")"

    @classmethod
    def apply_all_filters(cls, word):
        fword = word
        aux = set()
        iterable = [cls.nothing, cls.between_parenthesis]
        filters = powerset(iterable)
        for filt in filters:
            fword = word
            for f in filt:
                fword = f(fword)
            aux.add(fword)
        return list(aux)


def powerset(iterable):
    return chain.from_iterable(combinations(iterable, r) for r in range(len(iterable)+1))

  
