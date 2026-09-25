"""โรงแรมกลางกรุง ไม่มีชั้น 13"""


def get_p1(digits):
    """คำนวณหลักแรก"""
    for idx, val in enumerate(digits):
        if val > 5:
            return ["9", "10", "11", "12", "14"][idx]
    return "13"


def get_p2(n_str, digits):
    """คำนวณหลักที่สอง"""
    d1, d2, _, d4, d5 = digits
    if n_str == n_str[::-1]:
        if (d1 + d5) > 5:
            return "1"
        if (d2 * d4) > 5:
            return "2"
        return "0"

    div_result = (d1 // d5) if d5 else 0
    if div_result > 5:
        return "1"
    if (d2 - d5) > 5:
        return "2"
    return "0"


def get_p3(digits):
    """คำนวณหลักที่สาม"""
    if sum(digits) > 25:
        return "1"

    prod = 1
    for digit in digits:
        prod *= digit

    if prod > 55:
        return "2"
    return "0"


def main():
    """main"""
    n_str = input().strip().zfill(5)
    digits = [int(ch) for ch in n_str]

    p1 = get_p1(digits)
    p2 = get_p2(n_str, digits)
    p3 = get_p3(digits)

    print(f"{p1}{p2}{p3}")


main()
