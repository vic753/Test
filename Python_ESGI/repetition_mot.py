
import argparse
import sys

print(sys.argv)

parser = argparse.ArgumentParser(description='Répète mots')
parser.add_argument("--mot")
parser.add_argument("--n", type=int, required=True, help="Nombre de répétitions")
args = parser.parse_args()

for i in range (args.n):
    print(args.mot)
