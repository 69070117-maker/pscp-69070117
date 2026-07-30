"""3019"""
def main():
    """"main"""
    char = input()
    num = input()
    if char == "H" and num == "4567" :
        print("safe unlocked")
    elif char != "H" and num == "4567" :
        print("safe locked - change char")
    elif char == "H" and num != "4567" :
        print("safe locked - change digit")
    elif char == "h" and num != "4567" :
        print("safe locked ")
    else:
        print("safe locked")
main()
