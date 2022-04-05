import argparse
from ast import arg
import re
import os
from tracemalloc import stop

parser = argparse.ArgumentParser()
parser.add_argument('-i')
#parser.add_argument('-o')
args = parser.parse_args()

with open(args.i, 'r') as f:
    contents = f.read().split('\n\n')
for index, element in enumerate(contents):
    with open(f'input_dir/sentence{index}.ssf', 'w') as file:
        file.write(element)

"""
awk 'BEGIN{i++} !NF{++i;next} {print > "filename"i".txt"}' mor-51-100-posn-name.txt
"""
