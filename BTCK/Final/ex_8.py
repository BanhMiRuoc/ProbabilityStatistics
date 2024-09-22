"""
Sử dụng câu lệnh sau để chạy code: python 52200205_52200051_52200033_8.py
"""

# Hiện thực bài toán thông qua 2 hàm extended_gcd và mod_inverse
def extended_gcd(a, b):
    """Trả về GCD của a và b, cùng với các hệ số x và y sao cho ax + by = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def mod_inverse(a, n):
    """Trả về nghịch đảo modulo của a modulo n sử dụng thuật toán Euclid mở rộng"""
    gcd, x, y = extended_gcd(a, n)
    if gcd != 1:
        raise ValueError(f"Không tồn tại nghịch đảo modulo cho {a} modulo {n}, vì chúng không nguyên tố cùng nhau.")
    else:
        # x có thể là số âm, nên chúng ta lấy modulo n để đảm bảo kết quả dương
        return x % n

# Kiểm tra chương trình bằng dữ liệu mẫu
sample_a = 5
sample_n = 288
inverse = mod_inverse(sample_a, sample_n)
print(f"Nghịch đảo modulo của {sample_a} modulo {sample_n} là {inverse}")

# Kiểm tra kết quả
if((sample_a * inverse) % sample_n == 1):
    print(f"Hậu kiểm kết quả, phép tính ({sample_a} * {inverse}) % {sample_n} = {(sample_a * inverse) % sample_n} cho thấy phép tính nghịch đảo này là ĐÚNG")
else:
    print(f"Hậu kiểm kết quả, phép tính ({sample_a} * {inverse}) % {sample_n} != {(sample_a * inverse) % sample_n} cho thấy phép tính nghịch đảo này là SAI")

