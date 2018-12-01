from functools import reduce

f = open('./input.txt')
contents = list(f.readlines())

frequencies = set()
cur_freq = 0
i = 0

while True:
    if i == len(contents):
        i = 0
    cur_freq += int(contents[i])
    if cur_freq in frequencies:
        print(cur_freq)
        break
    else:
        frequencies.add(cur_freq)

    i += 1