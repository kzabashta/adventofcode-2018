from functools import reduce

f = open('./input.txt')
contents = list(f.readlines())

twice_count = 0
thrice_count = 0

for line in contents:
    counts = {}

    l_twice = []
    l_thrice = []

    for letter in line:
        if not letter in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    
    for k, v in counts.items():
        if v == 2:
            l_twice.append(k)
        if v == 3:
            l_thrice.append(k)
    
    if len(l_twice) > 0:
        twice_count += 1
    
    if len(l_thrice) > 0:
        thrice_count += 1

checksum = twice_count * thrice_count
print(checksum)
