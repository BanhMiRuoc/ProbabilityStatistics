from fractions import Fraction
S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam')
, ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]

def P(event, space):
    return Fraction(len(event), len(space))

A = [s for s in S if s.count('Thanh') == 1]
print(A)

B = [s for s in S if s.count('Nữ') == 1]
print(B)

A_B = set(A) & set(B)
P_A = P(A, S)
P_B = P(B, S)
P_A_B = P(A_B, S)
print(P(A_B, B))