"""Roman3065"""
def main():
    """main"""
    number = int(input())
    if  1 <= number <= 9 :
        if number == 1 :
            print("I")
        elif number == 2:
            print("II")
        elif number == 3:
            print("III")
        elif number == 4:
            print("IV")
        elif number == 5:
            print("V")
        elif number == 6:
            print  ("VI")
        elif number == 7:
            print("VII")
        elif number == 8:
            print("VIII")
        elif number == 9:
            print("IX")
    elif number < 0 :
        print( "Error : Please input positive number")
    else :
        print("Error : Out of range")
main()
