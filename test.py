from filter import Prefilter, Postfilter 
from rule import rules

maxlevel = 1
words = ['lucas','test']
# for word in words:
#     print(word)
#     for prefilterWord in Prefilter.apply_all_filters(word):
#         for rule in Rule.all_rules():
#             for ruleWord in rule(prefilterWord):
#                 for postfilterWord in Postfilter.apply_all_filters(ruleWord):
#                     print(postfilterWord)



for word in words:
    for rule in rules:
        if rule.level <= maxlevel:
            print(rule.level)
            #[print(i) for i in rule.rule(word)]

