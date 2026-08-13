"""mad unicorn"""
def main():
    """flash"""
    start, stop = input().split()
    km = float(input())
    price = 0
    if start == "BKK" and stop == "CNX":
        price = 10 + 30*km
        print(f"{price:.2f}")
    elif start == "BKK" and stop == "PKT":
        price = 25 + 50*km
        print(f"{price:.2f}")
    elif start == "CNX" and stop == "UBP":
        price = 15 + 40*km
        print(f"{price:.2f}")
    elif start == "PKT" and stop == "CNX":
        price = 30 + 60*km
        print(f"{price:.2f}")
    elif start == "UBP" and stop == "PKT":
        price = 40 + 70*km
        print(f"{price:.2f}")
    elif start == "UBP" and stop == "BKK":
        price = 20 + 40*km
        print(f"{price:.2f}")
    else:
        print("Error")
main()
