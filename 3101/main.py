"""WATER STATUS"""
def main():
    """3101"""
    temp = int(input())
    unit = input().upper()

    if unit == "C":
        print_c(temp)
    elif unit == "F":
        print_f(temp)


def print_c(temp):
    """C"""
    if temp <= 0:
        print("solid")
    elif temp >= 100:
        print("gas")
    else:
        print("liquid")


def print_f(temp):
    """F"""
    if temp <= 32:
        print("solid")
    elif temp >= 212:
        print("gas")
    else:
        print("liquid")
main()
