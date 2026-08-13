"""3036"""
import math
def main():
    """main"""
    N = int(input())
    r = math.isqrt(N - 1) + 1    # หาว่าอยู่ชั้นไหน
    c = N - (r - 1) ** 2          # ดูว่าอยู่ลำดับไหนในชั้นนั้น

    # ชี้ขึ้น (c % 2 != 0) ใช้ 2*r - 2 / ชี้ลง ใช้ 2*r - 3
    print(2 * r - 2 if c % 2  else 2 * r - 3)
main()
