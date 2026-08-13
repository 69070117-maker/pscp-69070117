"""Taxi"""
def main():
    """more than 10km price = 8/km"""
    km = int(input())
    pr = 35
    if km == 1:
        pr = 35
    elif not km:
        pr = 0
    elif 1 < km <= 10:
        pr = pr + ((km-1)*5)
    elif km > 10 :
        pr = pr + 45 + ((km-10)*8)
    print(pr)
main()
