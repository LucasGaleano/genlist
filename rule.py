
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



@dataclass
class Rules(list):

    def show_rules(self, maxLevel):
        print('Rules')
        for rule in self:
            if not rule.prefilter and not rule.postfilter and rule.level_lower_than(maxLevel):
                print(rule.name, '-', rule.description, '-', rule.level)
        print()

        
        print('Prefilters')
        for rule in self:
            if rule.prefilter and rule.level_lower_than(maxLevel):
                print(rule.name, '-', rule.description, '-', rule.level)
        print()

        print('PostFilters')
        for rule in self:
            if rule.postfilter and rule.level_lower_than(maxLevel):
                print(rule.name, '-', rule.description, '-', rule.level)
        print()

    def prefilters(self, maxLevel):
        return [rule for rule in self if rule.prefilter if rule.level_lower_than(maxLevel)]
        
    def apply_prefilters(self, word):
        result = set()
        aux = []
        for subsetPrefilters in all_subset(self.prefilters(5)):
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

rules.append(Rule('append_date', 1, append_date, 'Append dates numbers at the end'))


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


##### PostFilter #####

def between_parenthesis(word):
    yield '(' + word + ')'

rules.append(Rule('between_parenthesis', 1, between_parenthesis, 'Puts word between parenthesis', postfilter=True))


