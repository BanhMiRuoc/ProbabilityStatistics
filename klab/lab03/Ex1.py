from fractions import Fraction
S = {'MMM', 'FFF', 'MMF', 'MFM', 'FMM', 'FFM', 'FMF', 'MFF'}

def elementsSpace():
    return len(S)
# print(elementsSpace())
B = {s for s in S if s.count('F') >= 1}
print(B)
A = {q for q in S if q.count('F') == 3}
A_B = set(A) & set(B)
print(A_B)

def P(event, space):
    return Fraction(len(event), len(space))
print(P(A_B, B))