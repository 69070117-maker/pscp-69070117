"""แสดงรูปสามเหลี่ยมมุมฉากด้วยเลข 0 และ 1"""


def main():
    """main"""
    n = int(input())

    for row in range(1, n + 1):
        line = []
        for col in range(1, row + 1):
            # เงื่อนไขเส้นรอบรูป 3 ด้าน:
            # 1. ด้านแนวตั้ง (col == 1)
            # 2. ด้านแนวนอน (row == n)
            # 3. ด้านแนวทแยง (row == col)
            if col == 1 or row == n or row == col:
                line.append("0")
            else:
                line.append("1")
        print("".join(line))


main()
