import itertools

def cross(A, B):
    return {a + b for a in A for b in B}
#4_a
urn = cross('W','12') | cross('B', '123') | cross('R', '1234')
#4_b
U3 = list(itertools.combinations(urn, 3))
#4_c
white1blue1red1 = []
for s in U3:
    countR = 0
    countB = 0
    countW = 0
    for i in range(0, 3):
        if s[i][0] == 'R':
            countR +=1
        if s[i][0] == 'B':
            countB +=1
        if s[i][0] == 'W':
            countW +=1
    if(countR == countB == countW == 1):
        white1blue1red1.append(s)  
print(len(U3))
print(white1blue1red1)
#4_d
P = (len(white1blue1red1)/len(U3))
print(P)