import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w','--words', nargs="+")
parser.add_argument('-l','--level', type=int, default=2)
parser.add_argument('-d','--debug', action='store_true')
parser.add_argument('-s','--show', action='store_true')

args = parser.parse_args()