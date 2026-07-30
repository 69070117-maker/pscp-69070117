"""3022"""
def main():
    """main"""
    tem = float(input())
    text_1 = input()
    text_2 = input()

    celsuis = 0.0

    if text_1 == 'C':
        celsuis = tem
    elif text_1 == 'K':
        celsuis = tem - 273.15
    elif text_1 == 'F':
        celsuis = (tem - 32) * 5 / 9
    elif text_1 == 'R':
        celsuis = (tem * 5 / 9 )  - 273.15

    ans = 0.0
    if text_2 == 'C':
        ans  = celsuis
    elif text_2 == 'K':
        ans = celsuis + 273.15
    elif text_2 == 'F':
        ans = celsuis * 9 / 5 + 32
    elif text_2 == 'R':
        ans = (celsuis + 273.15) * 9 / 5

    print(f"{ans:.2f}")
main()
