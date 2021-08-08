#! /usr/bin/env python3

from arguments import args
from rule import rules


def main():
    words = args.words
    maxlevel = args.level

    for word in words:
        for rule in rules:
            if rule.level <= maxlevel:
                [print(i) for i in rule.rule(word)]


if __name__ == "__main__":
    main()

