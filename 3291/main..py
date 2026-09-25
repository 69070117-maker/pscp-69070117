"""right arrow"""


def main():
    """right arrow"""
    k = int(input())
    n = int(input())

    # ครึ่งบนรวมแถวกลาง: ช่องว่างเพิ่มขึ้นเรื่อยๆ ตามค่า i (0, 1, 2, ...)
    for i in range(0, (n + 1) // 2):
        print(" " * i, end="")
        for _ in range(1, k + 1):
            print("*", end="")
        print()

    # ครึ่งล่าง: ช่องว่างลดลงเรื่อยๆ (n // 2 - i)
    for i in range(1, (n - (n + 1) // 2) + 1):
        print(" " * (n // 2 - i), end="")
        for _ in range(1, k + 1):
            print("*", end="")
        print()


main()
