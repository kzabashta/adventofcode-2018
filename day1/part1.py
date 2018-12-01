from functools import reduce

f = open('./input.txt')
contents = list(f.readlines())

freq = reduce((lambda x, y: int(x) + int(y)), contents)
print(freq)