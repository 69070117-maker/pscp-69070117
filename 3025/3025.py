"""nightmare"""
def main():
    """Season"""
    month = int(input())
    day = int(input())
    if day >= 21:
        month += 1
        if month > 12 :
            print("winter")
        elif 0 < month <= 3:
            print("winter")
        elif 3 < month <= 6:
            print("spring")
        elif 6 < month <= 9:
            print("summer")
        else:
            print("fall")

    else:
        if 0 < month <= 3:
            print("winter")
        elif 3 < month <= 6:
            print("spring")
        elif 6 < month <= 9:
            print("summer")
        else:
            print("fall")
main()
