E = {0, 1, 2, 3, 4, 5}
Ea = {1, 2, 3, 4, 5}
numbers = []
for i in Ea:
    for j in E:
        for k in E:
            number = i*100 + j*10 + k
            numbers.append(number)
# print(numbers)
num4digit = []
for a in Ea:
    for b in E:
        if a != b:
            for c in E:
                if b != c and a!= c:
                    for d in E:
                        if d != c and d!= b and d!= a:
                            num4digit.append(str(a)+str(b)+str(c)+str(d))
print(num4digit)