"""Ticket"""
def main():
    """3104"""
    age , day = input().split()
    age = int(age)
    if age < 5 :
        price = 0
    elif 5 <= age <= 18:
        price = 100
    else :
        price = 150

    if day == "Wed":
        price = price // 2
    print(price)
main()
