import argparse
from soupClass import *
# Create the parser
defaultOption = None
parser = argparse.ArgumentParser(description='Web Scrapping')
parser.add_argument(
                    'integers', 
                     metavar='Program Number(s)', 
                    type=list,
                    const=defaultOption, 
                    nargs='?',
                    help="The program(s) you want to run. They range from 1 to 4."
                    )

args = parser.parse_args()
# print(type(args.integers))
# print(args.integers)

sp = SOUP()
sp.start(args)