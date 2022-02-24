from itertools import groupby

input = input()

for c, items in groupby(input):
    print(tuple([len(list(items)), int(c)]), end = ' ')