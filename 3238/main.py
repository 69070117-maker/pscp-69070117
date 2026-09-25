"""Elon Musk - X-shape Drawer"""


def main():
    """main"""
    raw_input = input().strip().split()
    if len(raw_input) == 2:
        x = int(raw_input[0])
        k = raw_input[1]
    else:
        x = int(raw_input[0][:-1])
        k = raw_input[0][-1]

    center = x // 2

    for row in range(x):
        line = []
        for col in range(x):
            if row == col or row + col == x - 1:
                if k == "#":
                    line.append("#")
                else:
                    # คำนวณระยะห่างจากจุดศูนย์กลาง (center)
                    dist = abs(row - center)
                    # ตัวอักษรเริ่มจาก k แล้วบวกเพิ่มตามระยะห่าง
                    char_code = ord(k) + dist
                    line.append(chr(char_code))
            else:
                line.append("-")
        print("".join(line))


main()
