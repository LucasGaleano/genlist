import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w','--words', nargs="+")
parser.add_argument('-l','--level', type=int)

args = parser.parse_args()