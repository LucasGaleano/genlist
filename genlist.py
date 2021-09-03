#! /usr/bin/env python3

from arguments import args
from rule import rules


def main():

    maxlevel = args.level

    if args.show:
        rules.show_rules(maxlevel)

    if args.words:

        countWord = 0
        prefilterWords = list(args.words)
        for word in args.words:
            for output in rules.apply_prefilters(word, maxlevel):
                prefilterWords.append(output)
                if not args.debug:
                    print(output)
                countWord = countWord+1

        if args.debug:
            print(prefilterWords)
            print('count prefilters words: ', len(prefilterWords))
            print()
            print('Applied:')
            rules.show_rules(maxlevel)

        for prefilterWord in prefilterWords:
            for output in rules.apply_rules(prefilterWord, maxlevel):
                if not args.debug:
                    print(output)
                countWord = countWord+1

        print('count words: ', countWord)

if __name__ == "__main__":
    main()

