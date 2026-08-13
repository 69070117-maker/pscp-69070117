"""Bonus"""
def main():
    """3107"""
    position, old, slary = input().split()
    old = float(old)
    slary = float(slary)
    position = position.strip().upper()

    bonus = 0

    if position == "M":
        bonus = 1500
        if old < 5:
            bonus += slary * 0.06
        elif old <= 10:
            bonus += slary * 0.08
        else:
            bonus += slary * 0.10
    elif position == "B":
        bonus = 1000
        if old < 5:
            bonus += slary * 0.05
        elif old <= 10:
            bonus += slary * 0.06
        else:
            bonus += slary * 0.07
    elif position == "G":
        bonus = 500
        if old < 5:
            bonus += slary * 0.04
        elif old <= 10:
            bonus += slary * 0.05
        else:
            bonus += slary * 0.06

    print(int(round(bonus)))


main()
