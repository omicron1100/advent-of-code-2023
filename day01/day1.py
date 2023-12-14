import math

file = open("input", "r")

configurations = file.readlines()

sum = 0

for line in configurations:
    d1, d2 = "", ""
    for c in line:
        if c.isdigit():
            d1 = c
            break

    for r in line[::-1]:
        if r.isdigit():
            d2 = r
            break
    
    num = int(d1 + d2)
    sum += num

print(sum)
