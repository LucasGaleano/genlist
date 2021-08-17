#! /usr/bin/env python3

from arguments import args
from rule import rules


def main():
    words = args.words
    maxlevel = args.level

    prefilterWords = list()
    for word in words:
        for prefilter in rules.apply_prefilters(word):
            prefilterWords.append(prefilter)

    print('prefilterWords: ', prefilterWords)

    if args.debug:
        rules.show_rules(maxlevel)
    for prefilterWord in prefilterWords:
        for rule in rules:
            if rule.level_lower_than(maxlevel):
                if not args.debug:
                    [print(i) for i in rule.rule(prefilterWord)]

if __name__ == "__main__":
    main()

