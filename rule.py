
from dataclasses import dataclass
from itertools import combinations, chain

@dataclass
class Rule:

    name: str
    level: int
    rule: str #rule function
    description: str = ''
    prefilter: bool = False
    postfilter: bool = False
    
    def __hash__(self):
        return hash(self.rule)

    def level_lower_than(self, maxLevel):
        return self.level <= maxLevel

def all_subset(iterable):
    subsets =  list(chain.from_iterable(combinations(iterable, r) for r in range(len(iterable)+1)))
    return set(list(subsets) + [tuple(reversed(i)) for i in subsets])

def all_subset_no_repetable(iterable):
    return  list(chain.from_iterable(combinations(iterable, r) for r in range(1,len(iterable)+1)))



@dataclass
class Rules(list):

    maxLevel: int = 5

    def show_rules(self, maxLevel=None):
        print('Rules:')
        if maxLevel is None:
            maxLevel = self.maxLevel
        for rule in self:
            if not rule.prefilter and not rule.postfilter and rule.level_lower_than(maxLevel):
                print(rule.name, '-', rule.description, '- level: ', rule.level)
        print()

        
        print('Prefilters:')
        for rule in self:
            if rule.prefilter and rule.level_lower_than(maxLevel):
                print(rule.name, '-', rule.description, '-', rule.level)
        print()

        print('PostFilters:')
        for rule in self:
            if rule.postfilter and rule.level_lower_than(maxLevel):
                print(rule.name, '-', rule.description, '-', rule.level)
        print()

    def rules(self, maxLevel=None):
        if maxLevel is None:
            maxLevel = self.maxLevel
        return [rule for rule in self if not rule.prefilter and not rule.postfilter and rule.level_lower_than(maxLevel)]

    def apply_rules(self, word, maxLevel=None):
        if maxLevel is None:
            maxLevel = self.maxLevel
        for rule in self.rules(maxLevel):
            if rule.level_lower_than(maxLevel):   
                for output in rule.rule(word):
                    yield output


    def prefilters(self, maxLevel=None):
        if maxLevel is None:
            maxLevel = self.maxLevel
        return [rule for rule in self if rule.prefilter and rule.level_lower_than(maxLevel)]

    def postfilter(self, maxLevel=None):
        if maxLevel is None:
            maxLevel = self.maxLevel
        return [rule for rule in self if rule.postfilter and rule.level_lower_than(maxLevel)]
        
    def apply_prefilters(self, word, maxLevel=None):
        result = set()
        aux = []
        if maxLevel is None:
            maxLevel = self.maxLevel
        for subsetPrefilters in all_subset(self.prefilters(maxLevel)):
            prefilterWords = set([word])
            result.update(aux)
            aux = []
            for prefilter in subsetPrefilters:
                prefilterWords.update(aux)
                for prefilterword in prefilterWords:
                    for auxword in prefilter.rule(prefilterword):                 
                        aux.append(auxword)
                       
        return result



rules = Rules()


##### Rules ######

def append_4num(word):
    for num in range(1000,10000):
        if num not in range(1900,2050):
            yield word+str(num)

rules.append(Rule('append_4num', 2, append_4num, 'Append 4 numbers at the end'))


def append_common_num(word):
    for num in list(range(1,100))+[123,1234,12345,123456]:
        yield word+str(num)

rules.append(Rule('append_common_num', 1, append_common_num, 'Append commons numbers at the end'))


def append_date(word):
    for date in range(1900,2050):
        yield word+str(date)

rules.append(Rule('append_date', 2, append_date, 'Append dates numbers at the end'))


def append_special_char(word): 
    for char in ['!','@','*','$','.']: 
        yield word+char 

rules.append(Rule('append_special_char', 1, append_special_char, 'Append specials characters at the end', prefilter=True, postfilter=True))




##### PreFilter #####

def capitalize_word(word):
    yield word.capitalize()

rules.append(Rule('capitalize_word', 1, capitalize_word, 'Capitalize word', prefilter=True))

def uppercase_word(word):
    yield word.upper()

rules.append(Rule('uppercase_word', 1, uppercase_word, 'Uppercase word', prefilter=True ))

def leet(word):
    map_leet = {'a':'4','e':'3','i':'1','o':'0', 's':'$','l':'1'}

    leet = []
    for i, letter in enumerate(word):
        if letter in list(map_leet.keys()):
            leet.append(i)


    for comb in all_subset_no_repetable(leet):
        aux = list(word)
        for i in comb:
            aux[i] = map_leet[aux[i]]
        yield ''.join(aux)

rules.append(Rule('leet', 3, leet, 'Leet word', prefilter=True ))


##### PostFilter #####

def between_parenthesis(word):
    yield '(' + word + ')'

rules.append(Rule('between_parenthesis', 1, between_parenthesis, 'Puts word between parenthesis', postfilter=True))


