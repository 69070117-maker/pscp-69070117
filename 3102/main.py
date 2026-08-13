"""3102feecar"""
def main():
    """3012"""
    year = int(input())
    CC = int(input())
    price = 0
    if 0 < year <= 1990 :
        if CC <= 1500 :
            price = 1250
        elif 1500 < CC <= 2000:
            price = 1400
        elif CC > 2000:
            price = 2000
    elif 1991 <= year <= 1999:
        if CC <= 1500 :
            price = 1100
        elif 1500 < CC <= 2000:
            price = 1300
        elif CC > 2000:
            price = 1700
    elif year >= 2000:
        if CC <= 1500 :
            price = 1000
        elif 1500 < CC <= 2000:
            price = 1200
        elif CC > 2000:
            price = 1500
    print(price)
main()
