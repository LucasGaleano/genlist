#! /usr/bin/env python3

from arguments import args
from rule import rules


def main():
    words = args.words
    maxlevel = args.level

    prefilterWords = list()
    for word in words:
        for prefilter in rules.prefilter():
            prefilterWords.append(prefilter(word))

    print(prefilterWords)

    # for word in words:
    #     for rule in rules:
    #         if rule.level <= maxlevel:
    #             [print(i) for i in rule.rule(word)]


if __name__ == "__main__":
    main()

