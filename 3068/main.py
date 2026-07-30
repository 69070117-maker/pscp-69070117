"""Leap year"""
def main():
    """3068"""
    year = int(input())
    if year > 1582:
        if not year % 400:
            print("yes")
        elif not year % 4 :
            if year % 100:
                print("yes")
            else :
                print("no")
    else :
        if not year % 4:
            print("yes")
        else :
            print("no")
main()
